import json

def parse_source_nodes(nodes):
    parsed_data = {
        "channels": [],
        "categories": {},
        "relationships": []
    }

    for node in nodes:
        metadata = node.metadata if hasattr(node, 'metadata') else {}
        node_text = node.text if hasattr(node, 'text') else ""

        # Extract channel information
        if "handle" in metadata:
            channel = {
                "handle": metadata["handle"],
                "url": metadata.get("url", ""),
                "followers": metadata.get("followers", ""),
                "score": metadata.get("score", 0)
            }
            parsed_data["channels"].append(channel)

        # Extract relationships
        if "kg_rel_texts" in metadata:
            for rel in metadata["kg_rel_texts"]:
                rel_parts = rel.strip("()").split(", ")
                if len(rel_parts) == 3:
                    relationship = {
                        "subject": rel_parts[0].strip("'"),
                        "predicate": rel_parts[1].strip("'"),
                        "object": rel_parts[2].strip("'")
                    }
                    parsed_data["relationships"].append(relationship)

                    # Categorize channels
                    if relationship["predicate"] == "BELONGS_TO":
                        category = relationship["object"]
                        channel = relationship["subject"]
                        if category not in parsed_data["categories"]:
                            parsed_data["categories"][category] = []
                        parsed_data["categories"][category].append(channel)

        # If the node text contains channel information, parse it
        if node_text.startswith("{") and node_text.endswith("}"):
            try:
                channel_info = eval(node_text)
                if isinstance(channel_info, dict) and "handle" in channel_info:
                    parsed_data["channels"].append(channel_info)
            except:
                pass  # If eval fails, just skip this node text

    return parsed_data

def parse_query_response(response_json):
    try:
        data = json.loads(response_json)
        source_nodes = data.get("nodes", [])
        return parse_source_nodes(source_nodes)
    except json.JSONDecodeError:
        print("Error: Invalid JSON")
        return None
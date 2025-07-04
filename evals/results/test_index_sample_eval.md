# Evaluation Report

## Metadata

- **Timestamp:** 2024-07-15T15:08:52.172345
- **Number of Queries Run:** 5
- **Total Documents Retrieved:** 20
- **Average Query Runtime:** 7.59 seconds
- **Total Runtime:** 37.96 seconds

## Query Engine Parameters

- **persist_dir:** ./persist_dir
- **eval_mode:** True
- **llm:** callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x31a3e7320> system_prompt=None messages_to_prompt=<function messages_to_prompt at 0x16fa1aac0> completion_to_prompt=<function default_completion_to_prompt at 0x16fc74900> output_parser=None pydantic_program_mode=<PydanticProgramMode.DEFAULT: 'default'> query_wrapper_prompt=None model='gpt-4-turbo' temperature=0.1 max_tokens=None logprobs=None top_logprobs=0 additional_kwargs={} max_retries=3 timeout=60.0 default_headers=None reuse_client=True api_key='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' api_base='https://api.openai.com/v1' api_version=''
- **embed_model:** model_name='text-embedding-ada-002' embed_batch_size=100 callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x31ac8a8a0> num_workers=None additional_kwargs={} api_key='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' api_base='https://api.openai.com/v1' api_version='' max_retries=10 timeout=60.0 default_headers=None reuse_client=True dimensions=None
- **response_mode:** compact
- **embedding_mode:** hybrid
- **similarity_top_k:** 25
- **reranker:** callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x31a3e7320> top_n=20 choice_select_prompt=PromptTemplate(metadata={'prompt_type': <PromptType.CHOICE_SELECT: 'choice_select'>}, template_vars=['context_str', 'query_str'], kwargs={}, output_parser=None, template_var_mappings=None, function_mappings=None, template="A list of documents is shown below. Each document has a number next to it along with a summary of the document. A question is also provided. \nRespond with the numbers of the documents you should consult to answer the question, in order of relevance, as well \nas the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.\nDo not include any documents that are not relevant to the question. \nExample format: \nDocument 1:\n<summary of document 1>\n\nDocument 2:\n<summary of document 2>\n\n...\n\nDocument 10:\n<summary of document 10>\n\nQuestion: <question>\nAnswer:\nDoc: 9, Relevance: 7\nDoc: 3, Relevance: 4\nDoc: 7, Relevance: 3\n\nLet's try this now: \n\n{context_str}\nQuestion: {query_str}\nAnswer:\n") choice_batch_size=10 llm=OpenAI(callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x31a3e7320>, system_prompt=None, messages_to_prompt=<function messages_to_prompt at 0x16fa1aac0>, completion_to_prompt=<function default_completion_to_prompt at 0x16fc74900>, output_parser=None, pydantic_program_mode=<PydanticProgramMode.DEFAULT: 'default'>, query_wrapper_prompt=None, model='gpt-4-turbo', temperature=0.1, max_tokens=None, logprobs=None, top_logprobs=0, additional_kwargs={}, max_retries=3, timeout=60.0, default_headers=None, reuse_client=True, api_key='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', api_base='https://api.openai.com/v1', api_version='')
- **parse_function:** custom_parse_choice_select_answer_fn
- **use_custom_reranker:** False

## Summary Table

| Metric | Value |
|--------|-------|
| Average Faithfulness | 0.60 |
| Average Relevancy | 0.80 |
| Average Number of Source Nodes | 4.00 |
| Average Query Runtime (s) | 7.59 |

## Detailed Summary Table

| Query | Faithfulness | Relevancy | # Source Nodes | Runtime (s) |
|-------|--------------|-----------|----------------|-------------|
| find gaming creators | ✅ 1.00 | 1.00 | 2 | 8.04 |
| who are the top beauty influencers? | ✅ 1.00 | 1.00 | 4 | 5.02 |
| list some popular tech reviewers | ❌ 0.00 | 0.00 | 6 | 10.70 |
| what are the trending fashion channels? | ✅ 1.00 | 1.00 | 6 | 8.79 |
| recommend some cooking YouTubers | ❌ 0.00 | 1.00 | 2 | 5.42 |

## Metric Definitions

- **Faithfulness:** Measures how well the response aligns with the information provided in the source documents. A score of 1.0 indicates perfect alignment, while 0.0 suggests significant deviation.
- **Relevancy:** Assesses how relevant the response is to the given query. A score of 1.0 indicates high relevance, while 0.0 suggests the response is off-topic or unrelated.
- **Source Nodes:** The number of documents or text chunks retrieved and used to generate the response.
- **Runtime:** The time taken to process the query and generate a response, measured in seconds.

## Detailed Query Results

### Query 1: find gaming creators

**Response:**

The gaming creators mentioned are:

1. @GAMINGWITHDEE, who can be found on YouTube at https://www.youtube.com/channel/UCtwORe9SxDw7C-QYFFZALdQ with 8.3K followers.
2. @PeepGamePopoff, available on YouTube at https://www.youtube.com/channel/UCVTBgi6QDUvoZScAsCFmyFQ with 5.5K followers.

**Source Nodes:**

Node 1:
```
{'handle': '@GAMINGWITHDEE', 'url': 'https://www.youtube.com/channel/UCtwORe9SxDw7C-QYFFZALdQ', 'followers': '8.3K', 'score': 65}
```

Node 2:
```
{'handle': '@PeepGamePopoff', 'url': 'https://www.youtube.com/channel/UCVTBgi6QDUvoZScAsCFmyFQ', 'followers': '5.5K', 'score': 69}
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 2
- Query Runtime: 8.04 seconds

### Query 2: who are the top beauty influencers?

**Response:**

The top beauty influencers mentioned are @FoxyMakeupTipsandTutorials, @SnehaSTheBeautyMadness, and @BeyondBeautyNatasha.

**Source Nodes:**

Node 1:
```
The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@FoxyMakeupTipsandTutorials', 'BELONGS_TO', 'Beauty')
('@TopnotchBeautyPriyankaSaha', 'BELONGS_TO', 'Beauty')
('@SnehaSTheBeautyMadness', 'BELONGS_TO', 'Beauty')
('@ArhamAksasMomChannel', 'BELONGS_TO', 'Beauty')
('@BeautyHacksOfficial', 'BELONGS_TO', 'Beauty')
('@BeyondBeautyNatasha', 'BELONGS_TO', 'Beauty')
('@beautyrecommended', 'BELONGS_TO', 'Beauty')
('@MarshaOnderstijn', 'BELONGS_TO', 'Beauty')
('@silverstopmotion', 'BELONGS_TO', 'Beauty')
('@SelenaGomezVEVO', 'BELONGS_TO', 'Beauty')
('@Dr. Vivek Joshi', 'BELONGS_TO', 'Beauty')
('@InfiniteShorts', 'BELONGS_TO', 'Beauty')
('@MrBeast Gaming', 'BELONGS_TO', 'Beauty')
('@ArpitaNathblog', 'BELONGS_TO', 'Beauty')
('@TheIdiotDope', 'BELONGS_TO', 'Beauty')
('@Fe4RLesssHD', 'BELONGS_TO', 'Beauty')
('@JoshKreuger', 'BELONGS_TO', 'Beauty')
('@FashionTips', 'BELONGS_TO', 'Beauty')
('@DIYByshikha', 'BELONGS_TO', 'Beauty')
('@jmarhodes90', 'BELONGS_TO', 'Beauty')
('@ipsydotcom', 'BELONGS_TO', 'Beauty')
('@JoshHarmon', 'BELONGS_TO', 'Beauty')
('@ImmyMaryam', 'BELONGS_TO', 'Beauty')
('@Y2KVEVO', 'BELONGS_TO', 'Beauty')
('@jaiden', 'BELONGS_TO', 'Beauty')
```

Node 2:
```
{'handle': '@FoxyMakeupTipsandTutorials', 'url': 'https://www.youtube.com/channel/UCWlYYTM0_kX0OUAOhptJ3yg', 'followers': '391K', 'score': 71}
```

Node 3:
```
{'handle': '@SnehaSTheBeautyMadness', 'url': 'https://www.youtube.com/channel/UCP3Dp2rGnmtrWjAro-FsxvA', 'followers': '1.2M', 'score': 71}
```

Node 4:
```
{'handle': '@BeyondBeautyNatasha', 'url': 'https://www.youtube.com/channel/UC8F5DukBhdBUkBGxXXJnYlw', 'followers': '198K', 'score': 80}
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 4
- Query Runtime: 5.02 seconds

### Query 3: list some popular tech reviewers

**Response:**

I don't have information on popular tech reviewers in the provided context.

**Source Nodes:**

Node 1:
```
{'handle': '@RevZillaTV', 'url': 'https://www.youtube.com/channel/UCLQZTXj_AnL7fDC8sLrTGMw', 'followers': '1.3M', 'score': 74}
```

Node 2:
```
{'handle': '@HypebeastTV', 'url': 'https://www.youtube.com/channel/UCmd52DyhaO4E1Cvy4RrHuew', 'followers': '1M', 'score': 81}
```

Node 3:
```
{'handle': '@TheBootGuyreviews', 'url': 'https://www.youtube.com/channel/UC9ERIHMtYnY-QwgYnbDFjXw', 'followers': '49K', 'score': 81}
```

Node 4:
```
{'handle': '@RobbysReviews', 'url': 'https://www.youtube.com/channel/UClQ34igfLn63JA2kKmSNqUQ', 'followers': '5K', 'score': 90}
```

Node 5:
```
{'handle': '@paulfrankvideo', 'url': 'https://www.youtube.com/channel/UC4z3aW1YnoHW_M5a437TmqA', 'followers': '4.1K', 'score': 89}
```

Node 6:
```
The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@Recommended Presh TV', 'BELONGS_TO', 'Beauty')
('@BeautyAndTheGeekVEVO', 'BELONGS_TO', 'Series')
('@TheBootGuyreviews', 'BELONGS_TO', 'Apparel')
('@Techbot Customs', 'BELONGS_TO', 'Apparel')
('@TheWatchGuysTV', 'BELONGS_TO', 'Watches')
('@Dr. Vivek Joshi', 'BELONGS_TO', 'Beauty')
('@paulfrankvideo', 'BELONGS_TO', 'Apparel')
('@Khari Bernard', 'BELONGS_TO', 'Apparel')
('@monstersreview', 'BELONGS_TO', 'Series')
('@MrBeast Gaming', 'BELONGS_TO', 'Beauty')
('@RobbysReviews', 'BELONGS_TO', 'Apparel')
('@TheSomeGuyShow', 'BELONGS_TO', 'Series')
('@DevonReviewer', 'BELONGS_TO', 'Apparel')
('@OneUpReviewz', 'BELONGS_TO', 'Apparel')
('@WhatWeWatchin', 'BELONGS_TO', 'Series')
('@truepinoy101', 'BELONGS_TO', 'Apparel')
('@WatchReview', 'BELONGS_TO', 'Watches')
('@Josh Graham', 'BELONGS_TO', 'Apparel')
('@HypebeastTV', 'BELONGS_TO', 'Apparel')
('@KurtzerTech', 'BELONGS_TO', 'Apparel')
('@Technoblade', 'BELONGS_TO', 'Beauty')
('@RevZillaTV', 'BELONGS_TO', 'Apparel')
('@JonPhenom', 'BELONGS_TO', 'Apparel')
('@jcheungtv', 'BELONGS_TO', 'Apparel')
('@TalkMenTV', 'BELONGS_TO', 'Apparel')
```

**Evaluation Results:**

- Faithfulness: 0.00 (Fail)
  - Explanation: NO
- Relevancy: 0.00
  - Explanation: NO
- Number of Source Nodes: 6
- Query Runtime: 10.70 seconds

### Query 4: what are the trending fashion channels?

**Response:**

Some of the trending fashion channels include @HypebeastTV, @StitchlessTV, @FH TV, and @ImHauteTV. These channels are known for their content related to apparel and fashion, and they have a significant number of followers and high scores indicating their popularity and engagement.

**Source Nodes:**

Node 1:
```
{'handle': '@HypebeastTV', 'url': 'https://www.youtube.com/channel/UCmd52DyhaO4E1Cvy4RrHuew', 'followers': '1M', 'score': 81}
```

Node 2:
```
The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@myfashioninspiration', 'BELONGS_TO', 'Apparel')
('@FashionDesignSuccess', 'BELONGS_TO', 'Apparel')
('@FashionistaBlogger', 'BELONGS_TO', 'Apparel')
('@FashionGoOfficial', 'BELONGS_TO', 'Apparel')
('@FASHIONINSIDERSCO', 'BELONGS_TO', 'Apparel')
('@RevengeFashionTV', 'BELONGS_TO', 'Apparel')
('@behindthebrandTV', 'BELONGS_TO', 'Apparel')
('@PrimitiveChannel', 'BELONGS_TO', 'Apparel')
('@TheFashionRunUp', 'BELONGS_TO', 'Apparel')
('@ksproductionstv', 'BELONGS_TO', 'Apparel')
('@FashionNewsLive', 'BELONGS_TO', 'Apparel')
('@AllthingsStyles', 'BELONGS_TO', 'Apparel')
('@Fashionhustler', 'BELONGS_TO', 'Apparel')
('@FashionDivaCC', 'BELONGS_TO', 'Apparel')
('@StitchlessTV', 'BELONGS_TO', 'Apparel')
('@DerekChaotv', 'BELONGS_TO', 'Apparel')
('@HypebeastTV', 'BELONGS_TO', 'Apparel')
('@FashionTips', 'BELONGS_TO', 'Beauty')
('@kidsupertv', 'BELONGS_TO', 'Apparel')
('@jcheungtv', 'BELONGS_TO', 'Apparel')
('@TalkMenTV', 'BELONGS_TO', 'Apparel')
('@ImHauteTV', 'BELONGS_TO', 'Apparel')
('@FESPATV', 'BELONGS_TO', 'Apparel')
('@FH TV', 'BELONGS_TO', 'Apparel')
('@VFWTV', 'BELONGS_TO', 'Apparel')
```

Node 3:
```
{'handle': '@StitchlessTV', 'url': 'https://www.youtube.com/channel/UCUPPR4uM2ERdeu22Lvr38NA', 'followers': '115K', 'score': 73}
```

Node 4:
```
{'handle': '@FH TV', 'url': 'https://www.youtube.com/channel/UCA9HVQ2EVSQe6a4PlXgd_mA', 'followers': '65.1K', 'score': 86}
```

Node 5:
```
{'handle': '@ImHauteTV', 'url': 'https://www.youtube.com/channel/UC0R_Ba1tcH_1aNMLZ4xPLmw', 'followers': '52.2K', 'score': 91}
```

Node 6:
```
{'handle': '@FESPATV', 'url': 'https://www.youtube.com/channel/UC8rJM0_wQPWjSeSBhagQSkA', 'followers': '62.8K', 'score': 65}
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 6
- Query Runtime: 8.79 seconds

### Query 5: recommend some cooking YouTubers

**Response:**

You might enjoy checking out @KitchenMantra1 and @ryancantcook on YouTube for some cooking content. @KitchenMantra1 has a channel with a variety of recipes and cooking tips, and @ryancantcook offers a unique take on culinary adventures, appealing to a large audience.

**Source Nodes:**

Node 1:
```
{'handle': '@KitchenMantra1', 'url': 'https://www.youtube.com/channel/UCKtxve_RFYEvIGF7ev0a6wg', 'followers': '57.5K', 'score': 86}
```

Node 2:
```
{'handle': '@ryancantcook', 'url': 'https://www.youtube.com/channel/UCrSoIkZlyYlcdgKjyzePa7Q', 'followers': '1.6M', 'score': 87}
```

**Evaluation Results:**

- Faithfulness: 0.00 (Fail)
  - Explanation: NO
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 2
- Query Runtime: 5.42 seconds


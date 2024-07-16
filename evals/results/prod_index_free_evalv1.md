# Evaluation Report

## Metadata

- **Timestamp:** 2024-07-15T20:08:21.691328
- **Number of Queries Run:** 5
- **Total Documents Retrieved:** 30
- **Average Query Runtime:** 211.77 seconds
- **Total Runtime:** 1058.85 seconds
- **Index Load Time:** 843.03 seconds

## Query Engine Parameters

- **persist_dir:** /Users/kenneth/Desktop/lab/noometic_dev/indexes/7.15.24/persist_dir_11_39_june_12_free
- **eval_mode:** True
- **llm:** callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x1475bacc0> system_prompt=None messages_to_prompt=<function messages_to_prompt at 0x12461aa20> completion_to_prompt=<function default_completion_to_prompt at 0x1246d8860> output_parser=None pydantic_program_mode=<PydanticProgramMode.DEFAULT: 'default'> query_wrapper_prompt=None model='gpt-4-turbo' temperature=0.1 max_tokens=None logprobs=None top_logprobs=0 additional_kwargs={} max_retries=3 timeout=60.0 default_headers=None reuse_client=True api_key='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' api_base='https://api.openai.com/v1' api_version=''
- **embed_model:** model_name='BAAI/bge-small-en-v1.5' embed_batch_size=10 callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x132607a70> num_workers=None max_length=512 normalize=True query_instruction=None text_instruction=None cache_folder=None
- **response_mode:** compact
- **embedding_mode:** hybrid
- **similarity_top_k:** 25
- **reranker:** callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x1475bacc0> top_n=20 choice_select_prompt=PromptTemplate(metadata={'prompt_type': <PromptType.CHOICE_SELECT: 'choice_select'>}, template_vars=['context_str', 'query_str'], kwargs={}, output_parser=None, template_var_mappings=None, function_mappings=None, template="A list of documents is shown below. Each document has a number next to it along with a summary of the document. A question is also provided. \nRespond with the numbers of the documents you should consult to answer the question, in order of relevance, as well \nas the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.\nDo not include any documents that are not relevant to the question. \nExample format: \nDocument 1:\n<summary of document 1>\n\nDocument 2:\n<summary of document 2>\n\n...\n\nDocument 10:\n<summary of document 10>\n\nQuestion: <question>\nAnswer:\nDoc: 9, Relevance: 7\nDoc: 3, Relevance: 4\nDoc: 7, Relevance: 3\n\nLet's try this now: \n\n{context_str}\nQuestion: {query_str}\nAnswer:\n") choice_batch_size=10 llm=OpenAI(callback_manager=<llama_index.core.callbacks.base.CallbackManager object at 0x1475bacc0>, system_prompt=None, messages_to_prompt=<function messages_to_prompt at 0x12461aa20>, completion_to_prompt=<function default_completion_to_prompt at 0x1246d8860>, output_parser=None, pydantic_program_mode=<PydanticProgramMode.DEFAULT: 'default'>, query_wrapper_prompt=None, model='gpt-4-turbo', temperature=0.1, max_tokens=None, logprobs=None, top_logprobs=0, additional_kwargs={}, max_retries=3, timeout=60.0, default_headers=None, reuse_client=True, api_key='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', api_base='https://api.openai.com/v1', api_version='')
- **parse_function:** custom_parse_choice_select_answer_fn
- **index_load_time:** 843.0305788516998

## Summary Table

| Metric | Value |
|--------|-------|
| Average Faithfulness | 0.60 |
| Average Relevancy | 0.40 |
| Average Number of Source Nodes | 6.00 |
| Average Query Runtime (s) | 211.77 |

## Detailed Summary Table

| Query | Faithfulness | Relevancy | # Source Nodes | Runtime (s) |
|-------|--------------|-----------|----------------|-------------|
| find gaming creators | ✅ 1.00 | 1.00 | 9 | 59.20 |
| who are the top beauty influencers? | ❌ 0.00 | 0.00 | 6 | 21.25 |
| list some popular tech reviewers | ✅ 1.00 | 1.00 | 8 | 941.67 |
| what are the trending fashion channels? | ✅ 1.00 | 0.00 | 4 | 19.84 |
| recommend some cooking YouTubers | ❌ 0.00 | 0.00 | 3 | 16.89 |

## Metric Definitions

- **Faithfulness:** Measures how well the response aligns with the information provided in the source documents. A score of 1.0 indicates perfect alignment, while 0.0 suggests significant deviation.
- **Relevancy:** Assesses how relevant the response is to the given query. A score of 1.0 indicates high relevance, while 0.0 suggests the response is off-topic or unrelated.
- **Source Nodes:** The number of documents or text chunks retrieved and used to generate the response.
- **Runtime:** The time taken to process the query and generate a response, measured in seconds.

## Detailed Query Results

### Query 1: find gaming creators

**Response:**

Here are some gaming creators:

1. @erdoesgaming_
2. @gamingclipz777
3. @tabletopgameandhobby
4. @supernerdsgaming
5. @garett_the_gamer
6. @netsgamingcrew
7. @chriskgaming_
8. @thegamingcreed

**Source Nodes:**

Node 1:
```
Node ID: erdoesgaming_/
Text: ["Such an unfortunate time.. @janedav1rgin #erdoesgaming_ #for...", "Nostalgia from @yd1uzumaki and @oatmealzzzz5 rip ditty.it #e...", "#duet with @greaasyrats how dare she 😭 #erdoesgaming_ #foryo...", "My legs hurt 😭 dance by @Hugo Hilaire #erdoesgaming_ #foryou...", "Redid The dance because it needed more improvements! #erdoes...", "True though. I came back just to do this! Credits: @Nate #le...", "FIRE DANCE BY @johniecakes! #erdoesgaming_ #foryou #foryoupa...", "Roblox dance battle #erdoesga...(truncated)
Metadata:
  comments_c: [1820.0, 6760.0, 1730.0, 103.0, 11.0, 923.0, 37.0, 22.0, 22.0, 81.0, 7.0, 29.0, 36.0, 22.0, 10.0, 10...(truncated)
  country: US
  avg_comments: 563.24
  hearts_c: [659670.0, 476340.0, 175710.0, 955.0, 279.0, 341690.0, 1450.0, 1080.0, 638.0, 7770.0, 1010.0, 1740.0...(truncated)
  keys: ['gaming', 'dance', 'shuffle']
  bio: ERDoesGaming_ @erdoesgaming_ I'm ER This mask stuff is old
  language: English
  creator_age: 18-24
  avg_engagement: 26.24
  platform: tiktok
  last_activity: 2024-04-17T20:55:17.339350000
  video_urls_tk: ['https://www.tiktok.com/@erdoesgaming_/video/7157043937763609902/', 'https://www.tiktok.com/@erdoesgaming_/video/6825710404128263430/', 'https://www.tiktok.com/@erdoesgaming_/video/6906536398984154374/', 'https://www.tiktok.com/@erdoesgaming_/video/7355978090566159659/', 'https://www.tiktok.com/@erdoesgaming_/video/7331458748688469290/', 'https://www.tiktok.com/@erdoesgaming_/video/7324392716266130734/', 'https://www.tiktok.com/@erdoesgaming_/video/7210519758876183851/', 'https://www.tiktok.com/@erdoesgaming_/video/7209723143362022698/', 'https://www.tiktok.com/@erdoesgaming_/video/7206056741438573867/', 'https://www.tiktok.com/@erdoesgaming_/video/7195338119238028590/', 'https://www.tiktok.com/@erdoesgaming_/video/7192711402803465518/', 'https://www.tiktok.com/@erdoesgaming_/video/7177898229634272558/', 'https://www.tiktok.com/@erdoesgaming_/video/7171583479971433774/', 'https://www.tiktok.com/@erdoesgaming_/video/7168593788653325614/', 'https://www.tiktok.com/@erdoesgaming_/video/7167822641540140330/', 'https://www.tiktok.com/@erdoesgaming_/video/7164480450918878506/', 'https://www.tiktok.com/@erdoesgaming_/video/7160790676089752875/', 'https://www.tiktok.com/@erdoesgaming_/video/7154138897465855275/', 'https://www.tiktok.com/@erdoesgaming_/video/7151526899171200298/', 'https://www.tiktok.com/@erdoesgaming_/video/7148569517008997678/', 'https://www.tiktok.com/@erdoesgaming_/video/7146004025958239534/']
  hearts: [659670.0, 476340.0, 175710.0, 955.0, 279.0, 341690.0, 1450.0, 1080.0, 638.0, 7770.0, 1010.0, 1740.0...(truncated)
  engagements: [211.0, 154.1, 56.6, 0.34, 0.09, 109.29, 0.47, 0.35, 0.21, 2.5, 0.32, 0.56, 0.59, 1.13, 0.22, 11.53,...(truncated)
  engagements_c: [211.0, 154.1, 56.6, 0.34, 0.09, 109.29, 0.47, 0.35, 0.21, 2.5, 0.32, 0.56, 0.59, 1.13, 0.22, 11.53,...(truncated)
  id: 24695
  likes: 5000000
  avg_hearts_c: 81688.95
  image: https://p16-pu-useast8.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/26f9c43e32169d935509b1178a66b1a5~c5...(truncated)
  comments: [1820.0, 6760.0, 1730.0, 103.0, 11.0, 923.0, 37.0, 22.0, 22.0, 81.0, 7.0, 29.0, 36.0, 22.0, 10.0, 10...(truncated)
  avg_hearts: 81688.95
  url: https://www.tiktok.com/@erdoesgaming_/
  followers: 313500
  following: 907
  name: @erdoesgaming_
  avg_engagement_c: 26.24
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/6a020c53d6ba20774f87981507ec4fc9.jpg?x-expires=1...(truncated)
  avg_comments_c: 563.24
  earnings_post: 235.91-370.72
  creator_gender: male
Score: 10.000
```

Node 2:
```
Node ID: 07d0a61e-ed6c-42c8-82f8-bb44fcb8254a
Text: The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@grantsgamerecs', 'BELONGS_TO', 'instagram_boardgames')
('tabletopgameandhobby/', 'BELONGS_TO', 'tiktok_gaming')
('@beginner_gaming__', 'BELONGS_TO', 'instagram_gaming')
('weregonnalose_gaming/', 'BELONGS_TO', 'tiktok_gaming')
('@complexitygaming', 'BELONGS_TO', 'instagram_gaming')
('thegreenlandicgamer/', 'BELONGS_TO', 'tiktok_g...(truncated)
Metadata:
  kg_rel_texts: ["('@grantsgamerecs', 'BELONGS_TO', 'instagram_boardgames')", "('tabletopgameandhobby/', 'BELONGS_TO', 'tiktok_gaming')", "('@beginner_gaming__', 'BELONGS_TO', 'instagram_gaming')", "('weregonnalose_gaming/', 'BELONGS_TO', 'tiktok_gaming')", "('@complexitygaming', 'BELONGS_TO', 'instagram_gaming')", "('thegreenlandicgamer/', 'BELONGS_TO', 'tiktok_gamer')", "('@protostargames', 'BELONGS_TO', 'instagram_gaming')", "('josephnomasgaming/', 'BELONGS_TO', 'tiktok_gaming')", "('@indiegamelover', 'BELONGS_TO', 'instagram_gaming')", "('supernerdsgaming/', 'BELONGS_TO', 'tiktok_gaming')", "('@grantsgamerecs', 'BELONGS_TO', 'instagram_gamer')", "('larrythefordgamer/', 'BELONGS_TO', 'tiktok_gamer')", "('garett_the_gamer/', 'BELONGS_TO', 'tiktok_gaming')", "('thegamingguidee/', 'BELONGS_TO', 'tiktok_gaming')", "('animatorsvsgames/', 'BELONGS_TO', 'tiktok_gamer')", "('netsgamingcrew/', 'BELONGS_TO', 'tiktok_gaming')", "('thegamingcreed/', 'BELONGS_TO', 'tiktok_gaming')", "('gamingexploits/', 'BELONGS_TO', 'tiktok_gaming')", "('gamingclipz777/', 'BELONGS_TO', 'tiktok_gaming')", "('@dansgaming', 'BELONGS_TO', 'instagram_gaming')", "('chriskgaming_/', 'BELONGS_TO', 'tiktok_gaming')", "('erdoesgaming_/', 'BELONGS_TO', 'tiktok_gaming')", "('@emlsgaming', 'BELONGS_TO', 'instagram_gaming')", "('nacaodosgamers/', 'BELONGS_TO', 'tiktok_gamer')", "('epix.gaming7/', 'BELONGS_TO', 'tiktok_gaming')"]
  kg_rel_map: {'creators': [], 'gaming': [], 'find': []}
Score: 10.000
```

Node 3:
```
Node ID: gamingclipz777/
Text: ["#drdisrespect #fyp ", "#drdisrespect #drdisrespectlive #streamer #youtuber #youtube...", "#drdisrespect #drdisrespectlive #streamer #youtuber #youtube...", "#timthetatman #drdisrespect #fyp #foryou ", "#timthetatman #drdisrespect #fyp #foryou ", "#drdisrespect #fyp #foryou ", "#drdisrespect #fyp #foryou ", "This clip is so good #drdisrespect #fyp #foryou ", "#drdisrespect #timthetatman #nickmercs #fyp #foryou ", "#drdisrespect #timthetatman #fyp #foryou ", "#drdisrespect #timthetatman #fyp #fo...(truncated)
Metadata:
  comments_c: [1360.0, 957.0, 1790.0, 59.0, 135.0, 217.0, 16.0, 41.0, 24.0, 25.0, 44.0, 221.0, 9.0, 21.0, 77.0, 8....(truncated)
  country: US
  avg_comments: 249.39
  hearts_c: [196630.0, 313710.0, 444360.0, 3520.0, 12260.0, 42700.0, 1620.0, 1490.0, 2690.0, 4700.0, 9160.0, 560...(truncated)
  keys: ['gaming', 'streamer', 'clips']
  bio: gamingclipz777 @gamingclipz777 Road to 80k FOLLOWERS👀
  language: English
  avg_engagement: 64.41
  platform: tiktok
  last_activity: 2024-04-28T20:55:28.187231000
  video_urls_tk: ['https://www.tiktok.com/@gamingclipz777/video/7256370755028520235/', 'https://www.tiktok.com/@gamingclipz777/video/7234187338333621547/', 'https://www.tiktok.com/@gamingclipz777/video/7234600016260681006/', 'https://www.tiktok.com/@gamingclipz777/video/7362309166330907946/', 'https://www.tiktok.com/@gamingclipz777/video/7361910155899915562/', 'https://www.tiktok.com/@gamingclipz777/video/7361109271699787050/', 'https://www.tiktok.com/@gamingclipz777/video/7360669449000783150/', 'https://www.tiktok.com/@gamingclipz777/video/7360437173964819755/', 'https://www.tiktok.com/@gamingclipz777/video/7359380502190804270/', 'https://www.tiktok.com/@gamingclipz777/video/7358300387025210670/', 'https://www.tiktok.com/@gamingclipz777/video/7358285497313021230/', 'https://www.tiktok.com/@gamingclipz777/video/7358216640317738283/', 'https://www.tiktok.com/@gamingclipz777/video/7357563419714800942/', 'https://www.tiktok.com/@gamingclipz777/video/7357504864865242410/', 'https://www.tiktok.com/@gamingclipz777/video/7357488235251256622/', 'https://www.tiktok.com/@gamingclipz777/video/7357135070496410926/', 'https://www.tiktok.com/@gamingclipz777/video/7356747511698050347/', 'https://www.tiktok.com/@gamingclipz777/video/7356428887166930218/', 'https://www.tiktok.com/@gamingclipz777/video/7356422044893908267/', 'https://www.tiktok.com/@gamingclipz777/video/7356411433653079342/', 'https://www.tiktok.com/@gamingclipz777/video/7355998840526277930/', 'https://www.tiktok.com/@gamingclipz777/video/7355266409527528750/', 'https://www.tiktok.com/@gamingclipz777/video/7354903939512274219/']
  hearts: [196630.0, 313710.0, 444360.0, 3520.0, 12260.0, 42700.0, 1620.0, 1490.0, 2690.0, 4700.0, 9160.0, 560...(truncated)
  engagements: [257.8, 409.72, 580.92, 4.66, 16.14, 55.88, 2.13, 1.99, 3.53, 6.15, 11.98, 73.31, 1.21, 3.53, 22.95,...(truncated)
  engagements_c: [257.8, 409.72, 580.92, 4.66, 16.14, 55.88, 2.13, 1.99, 3.53, 6.15, 11.98, 73.31, 1.21, 3.53, 22.95,...(truncated)
  id: 28295
  likes: 9400000
  avg_hearts_c: 49219.87
  image: https://p19-pu-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/92dd4d868c1443c9f15f8d854a9d7be9~c5_...(truncated)
  comments: [1360.0, 957.0, 1790.0, 59.0, 135.0, 217.0, 16.0, 41.0, 24.0, 25.0, 44.0, 221.0, 9.0, 21.0, 77.0, 8....(truncated)
  avg_hearts: 49219.87
  url: https://www.tiktok.com/@gamingclipz777/
  followers: 76800
  following: 704
  name: @gamingclipz777
  avg_engagement_c: 64.41
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/1a71b935880909c4867457c5635650d7.jpg?x-expires=1...(truncated)
  avg_comments_c: 249.39
  earnings_post: 55.93-87.9
Score: 9.000
```

Node 4:
```
Node ID: tabletopgameandhobby/
Text: ["Wanna try out a new RPG? See what&rsquo;s being played a...", "Just a few of the best things at TableTop Game and Hobby♟🧩🀄️...", "We love returning faces! #gameexpansions #expansions #arkham...", "Walter goes by many different names around here. #walterthe...", "Replying to @Icebergalar This is close enough...right? #fung...", "&quot;I can&#039;t find any good two player games&am...", "Where else would you rather be? (Eat the Reich will be back...", "thank you in advance #watchmyboss #boardgam...(truncated)
Metadata:
  comments_c: [431.0, 30.0, 58.0, 0.0, 20.0, 1.0, 2.0, 6.0, 0.0, 4.0, 1.0, 2.0, 9.0, 2.0, 8.0, 2.0, 6.0, 2.0, 16.0...(truncated)
  country: US
  avg_comments: 26.61
  hearts_c: [42080.0, 1150.0, 4360.0, 72.0, 738.0, 42.0, 38.0, 63.0, 52.0, 83.0, 238.0, 180.0, 507.0, 139.0, 204...(truncated)
  keys: ['gaming', 'tabletop', 'hobby']
  bio: TableTop Game and Hobby @tabletopgameandhobby Kansas City’s Premier Game Store! 🎲📚🧩♟Scam alert! Bewa...(truncated)
  language: ['en', 'none', 'none']
  avg_engagement: 5.87
  platform: tiktok
  last_activity: 2024-06-09T09:02:02.127964000
  video_urls_tk: ['https://www.tiktok.com/@tabletopgameandhobby/video/7232361548956880174/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7113655522934394154/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7112542897240837422/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7376767325145402667/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7376399405286509866/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7375949174673607978/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7375653430590999854/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7375314333535980842/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7374915253731101994/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7374544941218909483/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7374198333855894826/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7373798641284271403/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7373353172892634414/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7373056497086893354/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7372693844225199402/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7372320075237346602/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7371945890392591659/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7371582768771370283/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7371201194926017834/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7370755689045593387/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7370476453168713002/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7370091276252810542/', 'https://www.tiktok.com/@tabletopgameandhobby/video/7369718710199782698/']
  hearts: [42080.0, 1150.0, 4360.0, 72.0, 738.0, 42.0, 38.0, 63.0, 52.0, 83.0, 238.0, 180.0, 507.0, 139.0, 204...(truncated)
  engagements: [110.71, 3.07, 11.51, 0.19, 1.97, 0.11, 0.1, 0.18, 0.14, 0.23, 0.62, 0.47, 1.34, 0.37, 0.55, 0.35, 0...(truncated)
  engagements_c: [110.71, 3.07, 11.51, 0.19, 1.97, 0.11, 0.1, 0.18, 0.14, 0.23, 0.62, 0.47, 1.34, 0.37, 0.55, 0.35, 0...(truncated)
  id: 72701
  likes: 375900
  avg_hearts_c: 2227.30
  image: https://p16-pu-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/7351395836665790507~c5_720x720.jpeg
  comments: [431.0, 30.0, 58.0, 0.0, 20.0, 1.0, 2.0, 6.0, 0.0, 4.0, 1.0, 2.0, 9.0, 2.0, 8.0, 2.0, 6.0, 2.0, 16.0...(truncated)
  avg_hearts: 2227.30
  url: https://www.tiktok.com/@tabletopgameandhobby/
  followers: 38400
  following: 50
  name: @tabletopgameandhobby
  avg_engagement_c: 5.87
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/ad5885cbfe163bb9be2f6986584a23ab.jpg?x-expires=1...(truncated)
  avg_comments_c: 26.61
  earnings_post: 28.25-44.39
Score: 8.000
```

Node 5:
```
Node ID: supernerdsgaming/
Text: ["Oddworld Abes Oddyess on the PS1 I got asked for this game ...", "Well everyone asked for it so here&rsquo;s me locking th...", "Reply to @lunchboxlol let&rsquo;s level jump #aladdin #s...", "Star trekking across the universe with Star Trek The Next Ge...", "Lets be a doctor with Trauma Center Second Opinion #traumac...", "Checking out the retro game selection in cex Liverpool i was...", "What an amazing handheld Zelda adventure #zelda #zeldalinks...", "Mario Kart Wii is an absolute brilliant ...(truncated)
Metadata:
  comments_c: [2220.0, 1530.0, 630.0, 5.0, 10.0, 6.0, 3.0, 8.0, 15.0, 17.0, 8.0, 4.0, 2.0, 19.0, 10.0, 9.0, 4.0, 1...(truncated)
  country: GB
  avg_comments: 200.13
  hearts_c: [34010.0, 42940.0, 120230.0, 86.0, 58.0, 88.0, 64.0, 46.0, 109.0, 125.0, 48.0, 81.0, 103.0, 112.0, 8...(truncated)
  keys: ['retro', 'gaming', 'nostalgia']
  bio: Supernerd Simon @supernerdsgaming 🎮 Simon playing retro video daily on live come in and say hi 🎮
  language: English
  creator_age: 25-34
  avg_engagement: 8.13
  platform: tiktok
  last_activity: 2024-05-01T10:15:24.800217000
  video_urls_tk: ['https://www.tiktok.com/@supernerdsgaming/video/7247483217320742171/', 'https://www.tiktok.com/@supernerdsgaming/video/7149141213247999238/', 'https://www.tiktok.com/@supernerdsgaming/video/7090125619878464773/', 'https://www.tiktok.com/@supernerdsgaming/video/7363404269413862689/', 'https://www.tiktok.com/@supernerdsgaming/video/7363303631124253984/', 'https://www.tiktok.com/@supernerdsgaming/video/7363017172437847328/', 'https://www.tiktok.com/@supernerdsgaming/video/7362575294844144929/', 'https://www.tiktok.com/@supernerdsgaming/video/7362281008105934113/', 'https://www.tiktok.com/@supernerdsgaming/video/7362201549646449953/', 'https://www.tiktok.com/@supernerdsgaming/video/7361903660567170337/', 'https://www.tiktok.com/@supernerdsgaming/video/7361752255281843488/', 'https://www.tiktok.com/@supernerdsgaming/video/7361538269215034657/', 'https://www.tiktok.com/@supernerdsgaming/video/7361408018262576417/', 'https://www.tiktok.com/@supernerdsgaming/video/7361085320751811873/', 'https://www.tiktok.com/@supernerdsgaming/video/7360794847864802592/', 'https://www.tiktok.com/@supernerdsgaming/video/7360733443879210272/', 'https://www.tiktok.com/@supernerdsgaming/video/7360433542364433697/', 'https://www.tiktok.com/@supernerdsgaming/video/7360262928836152609/', 'https://www.tiktok.com/@supernerdsgaming/video/7360058511268613408/', 'https://www.tiktok.com/@supernerdsgaming/video/7359947838098345248/', 'https://www.tiktok.com/@supernerdsgaming/video/7359672973357321504/', 'https://www.tiktok.com/@supernerdsgaming/video/7359573380984589600/', 'https://www.tiktok.com/@supernerdsgaming/video/7359152008324074784/']
  hearts: [34010.0, 42940.0, 120230.0, 86.0, 58.0, 88.0, 64.0, 46.0, 109.0, 125.0, 48.0, 81.0, 103.0, 112.0, 8...(truncated)
  engagements: [33.24, 40.8, 110.88, 0.08, 0.06, 0.09, 0.06, 0.05, 0.11, 0.13, 0.05, 0.08, 0.1, 0.12, 0.09, 0.09, 0...(truncated)
  engagements_c: [33.24, 40.8, 110.88, 0.08, 0.06, 0.09, 0.06, 0.05, 0.11, 0.13, 0.05, 0.08, 0.1, 0.12, 0.09, 0.09, 0...(truncated)
  id: 72233
  likes: 1100000
  avg_hearts_c: 8658.26
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/3fe1c8ed0b9e422a8e8c35183b13514a~c5_720x720.jpeg
  comments: [2220.0, 1530.0, 630.0, 5.0, 10.0, 6.0, 3.0, 8.0, 15.0, 17.0, 8.0, 4.0, 2.0, 19.0, 10.0, 9.0, 4.0, 1...(truncated)
  avg_hearts: 8658.26
  url: https://www.tiktok.com/@supernerdsgaming/
  followers: 109000
  following: 438
  name: @supernerdsgaming
  avg_engagement_c: 8.13
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/821c042d80c6bc0b62606356ba596ffa.jpg?x-expires=1...(truncated)
  avg_comments_c: 200.13
  earnings_post: 78.81-123.84
  creator_gender: male
Score: 7.000
```

Node 6:
```
Node ID: garett_the_gamer/
Text: ["VR Knockoffs of Popular Video Games 😅 #vr #videogames #callo...", "I need a new keyboard 😅 #Gaming #gamingkeyboard #keyboard ...", "The Xbox logo is sourdough bread 🤣 #xbox #playstation #Gamin...", "Black Ops 6 will be on Game Pass at Launch 🙌 #callofduty #xb...", "Why Neuralink scares me. . . 😬", "Poorly explaining popular video games 🤣 Part 3", "Is this Game the Apex Legends of VR? 🤔 #atlasendgames #vrgam...", "Product Review: Kiwi Design Comfort Head Strap for Meta Ques...", "Poorly Describ...(truncated)
Metadata:
  comments_c: [3270.0, 3820.0, 6140.0, 185.0, 1090.0, 44.0, 70.0, 51.0, 360.0, 32.0, 29.0, 33.0, 137.0, 165.0, 85....(truncated)
  country: US
  avg_comments: 773.91
  hearts_c: [449310.0, 338010.0, 812450.0, 2390.0, 15190.0, 790.0, 4900.0, 2120.0, 2760.0, 1360.0, 1110.0, 1340....(truncated)
  keys: ['vr', 'gaming', 'tech']
  bio: Garett @garett_the_gamer 🎮 VR | Gaming | Tech 👉 @Sail VR  ✉️ Email: contact.garett.gamer@gmail.com
  language: ['en', 'none', 'none']
  avg_engagement: 91.25
  platform: tiktok
  last_activity: 2024-06-09T09:08:36.480880000
  video_urls_tk: ['https://www.tiktok.com/@garett_the_gamer/video/7347022887259278638/', 'https://www.tiktok.com/@garett_the_gamer/video/7332995898781207854/', 'https://www.tiktok.com/@garett_the_gamer/video/7301772945221881130/', 'https://www.tiktok.com/@garett_the_gamer/video/7376761174358084906/', 'https://www.tiktok.com/@garett_the_gamer/video/7371562296096689454/', 'https://www.tiktok.com/@garett_the_gamer/video/7371126884912123182/', 'https://www.tiktok.com/@garett_the_gamer/video/7371164906445524270/', 'https://www.tiktok.com/@garett_the_gamer/video/7370458187339664686/', 'https://www.tiktok.com/@garett_the_gamer/video/7369082653741534506/', 'https://www.tiktok.com/@garett_the_gamer/video/7369726610519412010/', 'https://www.tiktok.com/@garett_the_gamer/video/7370079840109694250/', 'https://www.tiktok.com/@garett_the_gamer/video/7369342250976922923/', 'https://www.tiktok.com/@garett_the_gamer/video/7368601853753380138/', 'https://www.tiktok.com/@garett_the_gamer/video/7367485777489530154/', 'https://www.tiktok.com/@garett_the_gamer/video/7365988849492790570/', 'https://www.tiktok.com/@garett_the_gamer/video/7365220886057618731/', 'https://www.tiktok.com/@garett_the_gamer/video/7364909682827300142/', 'https://www.tiktok.com/@garett_the_gamer/video/7364170434151025962/', 'https://www.tiktok.com/@garett_the_gamer/video/7363395899306872106/', 'https://www.tiktok.com/@garett_the_gamer/video/7362304105789787435/', 'https://www.tiktok.com/@garett_the_gamer/video/7361555221417315630/', 'https://www.tiktok.com/@garett_the_gamer/video/7360784862682385707/']
  hearts: [449310.0, 338010.0, 812450.0, 2390.0, 15190.0, 790.0, 4900.0, 2120.0, 2760.0, 1360.0, 1110.0, 1340....(truncated)
  engagements: [533.07, 402.63, 964.18, 3.03, 19.18, 0.98, 5.85, 2.56, 3.67, 1.64, 1.34, 1.62, 4.14, 6.12, 1.77, 0....(truncated)
  engagements_c: [533.07, 402.63, 964.18, 3.03, 19.18, 0.98, 5.85, 2.56, 3.67, 1.64, 1.34, 1.62, 4.14, 6.12, 1.77, 0....(truncated)
  id: 28372
  likes: 3700000
  avg_hearts_c: 76700.68
  image: https://p19-pu-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/3f6b493cc86e4e965e9fa4bcaccb4d20~c5_...(truncated)
  comments: [3270.0, 3820.0, 6140.0, 185.0, 1090.0, 44.0, 70.0, 51.0, 360.0, 32.0, 29.0, 33.0, 137.0, 165.0, 85....(truncated)
  avg_hearts: 76700.68
  url: https://www.tiktok.com/@garett_the_gamer/
  followers: 84900
  following: 22
  name: @garett_the_gamer
  avg_engagement_c: 91.25
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/8141fe2cc27637b41bfcb2496453489e.jpg?x-expires=1...(truncated)
  avg_comments_c: 773.91
  earnings_post: 69.14-108.66
Score: 6.000
```

Node 7:
```
Node ID: netsgamingcrew/
Text: ["Tested over hundreds of games, here&rsquo;s how a @NBA 2...", "The ENDGAME jumpshot for all guard 6&rsquo;4 and under. ...", "What do YOU think we could have done differently offensively...", "Here&rsquo;s a basic quick hitter set that we used in a ...", "Chain 2-Way Tenacity to make plays ALL OVER THE COURT in @NB...", "We took on one of the leading scorers and MVP snub&helli...", "From playing your first video game as a kid to playing in fr...", "Find out this week during the @NBA 2K League ...(truncated)
Metadata:
  comments_c: [244.0, 382.0, 109.0, 0.0, 5.0, 1.0, 2.0, 3.0, 3.0, 0.0, 2.0, 2.0, 6.0, 2.0, 4.0, 1.0, 1.0, 3.0, 4.0...(truncated)
  country: CA
  avg_comments: 34.22
  hearts_c: [40020.0, 77740.0, 56130.0, 132.0, 186.0, 46.0, 45.0, 92.0, 97.0, 90.0, 125.0, 264.0, 315.0, 207.0, ...(truncated)
  keys: ['gaming', 'NetsGC', 'Brooklyn']
  bio: Brooklyn NetsGC @netsgamingcrew 
  language: English
  creator_age: 20-24
  avg_engagement: 30.04
  platform: tiktok
  last_activity: 2024-04-29T20:57:06.186346000
  video_urls_tk: ['https://www.tiktok.com/@netsgamingcrew/video/7320692114956766506/', 'https://www.tiktok.com/@netsgamingcrew/video/7319929191984565546/', 'https://www.tiktok.com/@netsgamingcrew/video/7214206282083913002/', 'https://www.tiktok.com/@netsgamingcrew/video/7362655263494556971/', 'https://www.tiktok.com/@netsgamingcrew/video/7362281832861355310/', 'https://www.tiktok.com/@netsgamingcrew/video/7361866335355194666/', 'https://www.tiktok.com/@netsgamingcrew/video/7361526545426418990/', 'https://www.tiktok.com/@netsgamingcrew/video/7361106750654860590/', 'https://www.tiktok.com/@netsgamingcrew/video/7360740504016850222/', 'https://www.tiktok.com/@netsgamingcrew/video/7360410208700468522/', 'https://www.tiktok.com/@netsgamingcrew/video/7359653466626723114/', 'https://www.tiktok.com/@netsgamingcrew/video/7359239543423356202/', 'https://www.tiktok.com/@netsgamingcrew/video/7356734271102537002/', 'https://www.tiktok.com/@netsgamingcrew/video/7356305964028562734/', 'https://www.tiktok.com/@netsgamingcrew/video/7353329890135002411/', 'https://www.tiktok.com/@netsgamingcrew/video/7352254649438866734/', 'https://www.tiktok.com/@netsgamingcrew/video/7347771248283372842/', 'https://www.tiktok.com/@netsgamingcrew/video/7346676401606561066/', 'https://www.tiktok.com/@netsgamingcrew/video/7346289215660952875/', 'https://www.tiktok.com/@netsgamingcrew/video/7345929099908549931/', 'https://www.tiktok.com/@netsgamingcrew/video/7345547199775853867/', 'https://www.tiktok.com/@netsgamingcrew/video/7345197255919717678/', 'https://www.tiktok.com/@netsgamingcrew/video/7328136693998046507/']
  hearts: [40020.0, 77740.0, 56130.0, 132.0, 186.0, 46.0, 45.0, 92.0, 97.0, 90.0, 125.0, 264.0, 315.0, 207.0, ...(truncated)
  engagements: [156.97, 304.57, 219.26, 0.51, 0.74, 0.18, 0.18, 0.37, 0.39, 0.35, 0.5, 1.04, 1.25, 0.81, 0.48, 0.28...(truncated)
  engagements_c: [156.97, 304.57, 219.26, 0.51, 0.74, 0.18, 0.18, 0.37, 0.39, 0.35, 0.5, 1.04, 1.25, 0.81, 0.48, 0.28...(truncated)
  id: 55718
  likes: 317300
  avg_hearts_c: 7670.35
  image: https://p16-c1-va.ibyteimg.com/tos-maliva-avt-0068/7335390847657050118~tplv-tiktokx-cropcenter-q:720...(truncated)
  comments: [244.0, 382.0, 109.0, 0.0, 5.0, 1.0, 2.0, 3.0, 3.0, 0.0, 2.0, 2.0, 6.0, 2.0, 4.0, 1.0, 1.0, 3.0, 4.0...(truncated)
  avg_hearts: 7670.35
  url: https://www.tiktok.com/@netsgamingcrew/
  followers: 25650
  following: 41
  name: @netsgamingcrew
  avg_engagement_c: 30.04
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/e64709d9431734b5dd3af67acaa99b48.jpg?x-expires=1...(truncated)
  avg_comments_c: 34.22
  earnings_post: 18.91-29.71
  creator_gender: male
Score: 5.000
```

Node 8:
```
Node ID: chriskgaming_/
Text: ["Horrible ahh aim💀#fortnite #season4fortnite #foryoupage #gam...", "Just straight violation 💀#warzoneclips #warzone2#gulag ", "Hes waiting&hellip;&hellip;.#fortnite #fortnitebr #g...", "I i woke up and got up fresh as hell on a monday😭🙏#fortnite ...", "And yall say this is the worst season😭#fortnite #chapter5sea...", "@Fortnite Official add this🙏#fortnite#fallout#chapter5season...", "Mike tyson lol#fortnitebattleroyale #fortniteclips #foryoupa...", "This shi was crazy asf#fortnitebattleroyale #...(truncated)
Metadata:
  comments_c: [2590.0, 5790.0, 2980.0, 4.0, 8.0, 1.0, 4.0, 3.0, 9.0, 928.0, 6.0, 20.0, 16.0, 0.0, 7.0, 8.0, 2.0, 5...(truncated)
  country: US
  avg_comments: 540.87
  hearts_c: [353810.0, 960640.0, 218850.0, 38.0, 214.0, 68.0, 120.0, 50.0, 98.0, 89570.0, 71.0, 724.0, 833.0, 11...(truncated)
  keys: ['fortnite', 'gaming', 'content']
  bio: CHRISKGAMING_ @chriskgaming_ Twitter/@chrisKgaming_  YTchrisKgaming🗣️  🎮Content creator 👾    😈🙏
  language: ['en', 'none', 'fr']
  avg_engagement: 190.23
  platform: tiktok
  last_activity: 2024-06-06T16:53:36.657627000
  video_urls_tk: ['https://www.tiktok.com/@chriskgaming_/video/7276750889749253422/', 'https://www.tiktok.com/@chriskgaming_/video/7255889408354815275/', 'https://www.tiktok.com/@chriskgaming_/video/7234260079955201326/', 'https://www.tiktok.com/@chriskgaming_/video/7374978577726672174/', 'https://www.tiktok.com/@chriskgaming_/video/7373835270627609898/', 'https://www.tiktok.com/@chriskgaming_/video/7373500124749729070/', 'https://www.tiktok.com/@chriskgaming_/video/7372731160230743339/', 'https://www.tiktok.com/@chriskgaming_/video/7369667067756219690/', 'https://www.tiktok.com/@chriskgaming_/video/7369055505668525354/', 'https://www.tiktok.com/@chriskgaming_/video/7368933139248418094/', 'https://www.tiktok.com/@chriskgaming_/video/7367962059067182378/', 'https://www.tiktok.com/@chriskgaming_/video/7367911847325928746/', 'https://www.tiktok.com/@chriskgaming_/video/7366847667990695214/', 'https://www.tiktok.com/@chriskgaming_/video/7366777911749119275/', 'https://www.tiktok.com/@chriskgaming_/video/7365669905871523118/', 'https://www.tiktok.com/@chriskgaming_/video/7365216666302696747/', 'https://www.tiktok.com/@chriskgaming_/video/7364867061044071723/', 'https://www.tiktok.com/@chriskgaming_/video/7363155366571478314/', 'https://www.tiktok.com/@chriskgaming_/video/7362162437812178222/', 'https://www.tiktok.com/@chriskgaming_/video/7361938573949635886/', 'https://www.tiktok.com/@chriskgaming_/video/7359672951341337899/', 'https://www.tiktok.com/@chriskgaming_/video/7357923746881097002/', 'https://www.tiktok.com/@chriskgaming_/video/7356675001971445035/']
  hearts: [353810.0, 960640.0, 218850.0, 38.0, 214.0, 68.0, 120.0, 50.0, 98.0, 89570.0, 71.0, 724.0, 833.0, 11...(truncated)
  engagements: [950.4, 2577.15, 591.55, 0.11, 0.59, 0.18, 0.33, 0.14, 0.29, 241.33, 0.21, 1.98, 2.26, 0.03, 0.47, 0...(truncated)
  engagements_c: [950.4, 2577.15, 591.55, 0.11, 0.59, 0.18, 0.33, 0.14, 0.29, 241.33, 0.21, 1.98, 2.26, 0.03, 0.47, 0...(truncated)
  id: 16524
  likes: 4600000
  avg_hearts_c: 70797.48
  image: https://p16.tiktokcdn-us.com/tos-useast5-avt-0068-tx/03d06fc46783db00dae820d25f60f18e~c5_720x720.jpe...(truncated)
  comments: [2590.0, 5790.0, 2980.0, 4.0, 8.0, 1.0, 4.0, 3.0, 9.0, 928.0, 6.0, 20.0, 16.0, 0.0, 7.0, 8.0, 2.0, 5...(truncated)
  avg_hearts: 70797.48
  url: https://www.tiktok.com/@chriskgaming_/
  followers: 37500
  following: 2330
  name: @chriskgaming_
  avg_engagement_c: 190.23
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/673920b632f475ee2687a0cee9b47413.jpg?x-expires=1...(truncated)
  avg_comments_c: 540.87
  earnings_post: 30.9-48.56
Score: 4.000
```

Node 9:
```
Node ID: thegamingcreed/
Text: ["How can the same franchise have worse parkour nearly 10 year...", "When they had better parkour 15 years ago, than they do now ...", "Evolution of parkour in Assassin&rsquo;s Creed Part 1 #v...", "Video games without a happy ending Part 4 #videogames #gamin...", "Video games without a happy ending Part 3 #videogames #gamin...", "Video games without a happy ending Part 2 #videogames #gamin...", "Video Games without a happy ending #videogames #gaming #game...", "How many did you know? #videogame...(truncated)
Metadata:
  comments_c: [9150.0, 3720.0, 3440.0, 26.0, 250.0, 546.0, 1270.0, 55.0, 132.0, 371.0, 103.0, 272.0, 60.0, 29.0, 3...(truncated)
  country: GB
  avg_comments: 1358.09
  hearts_c: [566390.0, 524540.0, 450080.0, 621.0, 13370.0, 25960.0, 56120.0, 5350.0, 14820.0, 9180.0, 8930.0, 26...(truncated)
  keys: ['gaming', 'parkour', 'video']
  bio: TheGamingCreed @thegamingcreed 300k  🎉  Nothing is true. Everything is permitted.
  language: English
  avg_engagement: 32.61
  platform: tiktok
  last_activity: 2024-05-01T20:10:14.357038000
  video_urls_tk: ['https://www.tiktok.com/@thegamingcreed/video/7255381441201114395/', 'https://www.tiktok.com/@thegamingcreed/video/7144303275754540293/', 'https://www.tiktok.com/@thegamingcreed/video/7252432373508263195/', 'https://www.tiktok.com/@thegamingcreed/video/7363696194167590177/', 'https://www.tiktok.com/@thegamingcreed/video/7363234824385072417/', 'https://www.tiktok.com/@thegamingcreed/video/7362816471942188320/', 'https://www.tiktok.com/@thegamingcreed/video/7362482739762695456/', 'https://www.tiktok.com/@thegamingcreed/video/7362216827063110944/', 'https://www.tiktok.com/@thegamingcreed/video/7361494515737234721/', 'https://www.tiktok.com/@thegamingcreed/video/7361115775429594401/', 'https://www.tiktok.com/@thegamingcreed/video/7360758160770092320/', 'https://www.tiktok.com/@thegamingcreed/video/7360482191752580385/', 'https://www.tiktok.com/@thegamingcreed/video/7360063383510453536/', 'https://www.tiktok.com/@thegamingcreed/video/7359669582069599520/', 'https://www.tiktok.com/@thegamingcreed/video/7359351154456694049/', 'https://www.tiktok.com/@thegamingcreed/video/7359228268215618848/', 'https://www.tiktok.com/@thegamingcreed/video/7358494529512623393/', 'https://www.tiktok.com/@thegamingcreed/video/7348522685456076065/', 'https://www.tiktok.com/@thegamingcreed/video/7348171520243518752/', 'https://www.tiktok.com/@thegamingcreed/video/7346690946253212960/', 'https://www.tiktok.com/@thegamingcreed/video/7342234684434287905/', 'https://www.tiktok.com/@thegamingcreed/video/7341092004438347041/', 'https://www.tiktok.com/@thegamingcreed/video/7340372126853041441/']
  hearts: [566390.0, 524540.0, 450080.0, 621.0, 13370.0, 25960.0, 56120.0, 5350.0, 14820.0, 9180.0, 8930.0, 26...(truncated)
  engagements: [189.7, 174.11, 149.48, 0.21, 4.49, 8.74, 18.92, 1.78, 4.93, 3.15, 2.98, 8.8, 1.84, 0.71, 2.87, 0.33...(truncated)
  engagements_c: [189.7, 174.11, 149.48, 0.21, 4.49, 8.74, 18.92, 1.78, 4.93, 3.15, 2.98, 8.8, 1.84, 0.71, 2.87, 0.33...(truncated)
  id: 75041
  likes: 19700000
  avg_hearts_c: 97589.22
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/14f0e279e119a06dee0d47f512f2e610~c5_720x720.jpeg
  comments: [9150.0, 3720.0, 3440.0, 26.0, 250.0, 546.0, 1270.0, 55.0, 132.0, 371.0, 103.0, 272.0, 60.0, 29.0, 3...(truncated)
  avg_hearts: 97589.22
  url: https://www.tiktok.com/@thegamingcreed/
  followers: 303400
  following: 69
  name: @thegamingcreed
  avg_engagement_c: 32.61
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/9691588d6333bffbfa8013135d985d92.jpg?x-expires=1...(truncated)
  avg_comments_c: 1358.09
  earnings_post: 262.14-411.93
Score: 3.000
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 9
- Query Runtime: 59.20 seconds

### Query 2: who are the top beauty influencers?

**Response:**

The top beauty influencers include Jacquelyn, A Nova Beleza, Samantha Blender, Laura Morris, and Wen Lozano.

**Source Nodes:**

Node 1:
```
Node ID: @mrs_mccready
Text: ["La Dolce Vita!🍅🛵🥖 @lightslacquer summer 2024 collection, Catch Me in Capri, is available now! @lightslacquer created Catch Me in Capri with its incredible community of Artists, so it’s a really special collection! Paint your summer dreams and take a Mediterranean vacation with these six new colors that totally embody summertime. The colors in this collection are so beautifully striking and vivid, and definitely illustrate what I would imagine a color palette should be for Catch Me in Capri! Th...(truncated)
Metadata:
  comments_c: [10.0, 7.0, 8.0, 12.0, 9.0, 13.0, 5.0, 13.0, 4.0, 7.0, 5.0, 8.0]
  avg_comments: 8.42
  hearts_c: [30.0, 34.0, 34.0, 46.0, 50.0, 46.0, 29.0, 47.0, 38.0, 53.0, 53.0, 43.0]
  keys: beauty
  bio: 💄Makeup and Skincare
FOHR Verified
📷Photography
jacquelynmccready@gmail.com
📍FL-MS@ipsyOS Creator
  language: ['en']
  posts: 2846
  avg_engagement: 0.16
  platform: instagram
  last_activity: 2 weeks ago
  hearts: [30.0, 34.0, 34.0, 46.0, 50.0, 46.0, 29.0, 47.0, 38.0, 53.0, 53.0, 43.0]
  engagements: [0.13, 0.13, 0.14, 0.19, 0.19, 0.19, 0.11, 0.19, 0.14, 0.19, 0.19, 0.17]
  post_thumbnails: ["https://sp1.pixwox.com/p/pt_6869731748173762694414_0_9a2c5e062a6f8c2ca5d8c061e8e96299.jpg?v/t39.30...(truncated)
  engagements_c: [0.13, 0.13, 0.14, 0.19, 0.19, 0.19, 0.11, 0.19, 0.14, 0.19, 0.19, 0.17]
  id: 48088
  avg_hearts_c: 41.92
  comments: [10.0, 7.0, 8.0, 12.0, 9.0, 13.0, 5.0, 13.0, 4.0, 7.0, 5.0, 8.0]
  url_pixwox: https://www.pixwox.com/profile/mrs_mccready/
  avg_hearts: 41.92
  sorted_time_posted: ["2 weeks ago", "1 months ago", "1 months ago", "1 months ago", "1 months ago", "2 months ago", "2 m...(truncated)
  url: https://www.instagram.com/mrs_mccready/
  followers: 30900
  following: 2126
  avg_engagement_c: 0.16
  fullname: Jacquelyn
  avg_comments_c: 8.42
  last_activity_datetime: 2024-05-24T23:45:42.974306000
  username: @mrs_mccready
Score: 10.000
```

Node 2:
```
Node ID: afd27699-441c-4066-89a4-776aa6ffd539
Text: The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@beautybrokerofficial', 'BELONGS_TO', 'instagram_consultancy')
('@beautybrokerofficial', 'BELONGS_TO', 'instagram_aesthetics')
('@browessence', 'BELONGS_TO', 'instagram_beauty influencer')
('@influencedbyprabhkirat', 'BELONGS_TO', 'instagram_makeup')
('@beautytalkby_janne', 'BELONGS_TO', 'instagram_"fashion"')
('@beautytalkby_jan...(truncated)
Metadata:
  kg_rel_texts: ["('@beautybrokerofficial', 'BELONGS_TO', 'instagram_consultancy')", "('@beautybrokerofficial', 'BELONGS_TO', 'instagram_aesthetics')", "('@browessence', 'BELONGS_TO', 'instagram_beauty influencer')", "('@influencedbyprabhkirat', 'BELONGS_TO', 'instagram_makeup')", '(\'@beautytalkby_janne\', \'BELONGS_TO\', \'instagram_"fashion"\')', '(\'@beautytalkby_janne\', \'BELONGS_TO\', \'instagram_"beauty",\')', "('@beautykillsmua', 'BELONGS_TO', 'instagram_makeupartist')", '(\'@earthbeautiesdaily\', \'BELONGS_TO\', "instagram_\'beauty\'")', "('@innerbeautybybel', 'BELONGS_TO', 'instagram_influencer')", "('taylorelizabethbeauty/', 'BELONGS_TO', 'tiktok_beauty')", "('taylorelizabethbeauty/', 'BELONGS_TO', 'tiktok_makeup')", "('@upkeepbeauty', 'BELONGS_TO', 'instagram_aesthetics')", "('@lipo__beauty', 'BELONGS_TO', 'instagram_influencer')", "('etherealbeauty_x/', 'BELONGS_TO', 'tiktok_celebrity')", "('meghancarybrown/', 'BELONGS_TO', 'tiktok_influencer')", "('@lianabeauty', 'BELONGS_TO', 'instagram_influencer')", "('@makeupbyevan', 'BELONGS_TO', 'instagram_celebrity')", "('@bustlebeauty', 'BELONGS_TO', 'instagram_celebrity')", "('@__bellabeautyy', 'BELONGS_TO', 'instagram_makeup')", "('@beautybyanniie', 'BELONGS_TO', 'instagram_makeup')", "('@beauty.at.best_', 'BELONGS_TO', 'instagram_women')", "('@besthairworld', 'BELONGS_TO', 'instagram_beauty')", "('looksxbeauty/', 'BELONGS_TO', 'tiktok_influencer')", "('__bexbeauty__/', 'BELONGS_TO', 'tiktok_makeup')", "('alyssalaur', 'BELONGS_TO', 'tiktok_beauty')"]
  kg_rel_map: {'beauty': [], 'influencers': [], 'top': []}
Score: 10.000
```

Node 3:
```
Node ID: @anovabeleza
Text: ["🚨ESSE POST MERECE SUA ATENÇÃO!\nEu nem sei como começar esse review… acho que na verdade todos os meus elogios não serão suficientes para descrever a perfeição dessa paleta Multi Funcional de @makeupforever .\nApesar de ser uma aquisição muito recente, já posso afirmar (sem medo de ser prematura com a minha opinião) que a paleta HD SKIN FACE ESSENTIAL foi uma das melhores descobertas que eu já tive e talvez vire um dos melhores produtos de maquiagem que já testei.\nEu comprei a paleta por pura...(truncated)
Metadata:
  comments_c: [91.0, 55.0, 56.0, 89.0, 71.0, 89.0, 83.0, 107.0, 80.0, 34.0, 125.0, 70.0]
  avg_comments: 79.17
  hearts_c: [527.0, 194.0, 292.0, 592.0, 526.0, 615.0, 513.0, 768.0, 818.0, 347.0, 1379.0, 447.0]
  keys: beauty
  bio: ▪️Cosméticos, Maquiagem Importada e Perfumes
▪️Encomendas e Produtos na Pronta Entrega 👇🏻
  posts: 219
  avg_engagement: 2.77
  platform: instagram
  last_activity: 1 weeks ago
  hearts: [527.0, 194.0, 292.0, 592.0, 526.0, 615.0, 513.0, 768.0, 818.0, 347.0, 1379.0, 447.0]
  engagements: [2.57, 1.04, 1.45, 2.84, 2.49, 2.93, 2.48, 3.65, 3.74, 1.59, 6.27, 2.15]
  engagements_c: [2.57, 1.04, 1.45, 2.84, 2.49, 2.93, 2.48, 3.65, 3.74, 1.59, 6.27, 2.15]
  post_thumbnails: ["https://sp1.pixwox.com/p/pt_6869586221462221414554_0_657d3edd87a09ee1d69df7c2bc152947.jpg?v/t51.29...(truncated)
  id: 4891
  avg_hearts_c: 584.83
  comments: [91.0, 55.0, 56.0, 89.0, 71.0, 89.0, 83.0, 107.0, 80.0, 34.0, 125.0, 70.0]
  url_pixwox: https://www.pixwox.com/profile/anovabeleza/
  avg_hearts: 584.83
  sorted_time_posted: ["1 weeks ago", "2 weeks ago", "2 weeks ago", "1 months ago", "2 months ago", "2 months ago", "3 mon...(truncated)
  url: https://www.instagram.com/anovabeleza/
  followers: 24000
  following: 874
  avg_engagement_c: 2.77
  avg_comments_c: 79.17
  fullname: A Nova Beleza | Maquiagem Importada
  last_activity_datetime: 2024-05-30T23:51:38.149446000
  username: @anovabeleza
Score: 9.000
```

Node 4:
```
Node ID: @asap.samantha
Text: ["The prettiest pink setting powder 🎀🩰✨ @flowerknows_global\n.\nReally, the whole brand is made for the coquette girlies, but this setting powder in particular is way too cute and has that perfect pink-bow coquette vibe 🎀\n.\n#kbeauty #flowerknows #coquette #coquetteaesthetic #coquettecore #koreanmakeup #kmakeup #settingpowder #pinksettingpowder #makeupessentials #makeuptrends #makeuptrend #trendingmakeup #viralmakeup #viralvideos #pinkaesthetic #prettymakeup", "It looks TOO REAL🩸✨ @makeuprevolu...(truncated)
Metadata:
  comments_c: [753.0, 2009.0, 26.0, 33.0, 27.0, 35.0, 57.0, 24.0, 45.0, 43.0, 37.0, 36.0]
  avg_comments: 260.42
  hearts_c: [1.2, 2.2, 180.0, 206.0, 151.0, 126.0, 248.0, 137.0, 159.0, 513.0, 232.0, 445.0]
  keys: influencer
  bio: 🇨🇦 Toronto | Sudbury
🤳 Content Creator@downtownsudbury🫧 AD/pr: samantha@aceinfluencers.com
  language: English
  creator_age: 25-34
  posts: 534
  avg_engagement: 0.47
  platform: instagram
  last_activity: 8 hours ago
  hearts: [1.2, 2.2, 180.0, 206.0, 151.0, 126.0, 248.0, 137.0, 159.0, 513.0, 232.0, 445.0]
  engagements: [0.77, 2.04, 0.21, 0.24, 0.18, 0.16, 0.31, 0.16, 0.21, 0.57, 0.27, 0.49]
  post_thumbnails: ["https://sp1.pixwox.com/p/pt_6871641458505114292414_0_eb534725fb96c8aeb297156b2c5e1b28.jpg?v/t51.29...(truncated)
  engagements_c: [0.77, 2.04, 0.21, 0.24, 0.18, 0.16, 0.31, 0.16, 0.21, 0.57, 0.27, 0.49]
  id: 6105
  avg_hearts_c: 200.03
  comments: [753.0, 2009.0, 26.0, 33.0, 27.0, 35.0, 57.0, 24.0, 45.0, 43.0, 37.0, 36.0]
  url_pixwox: https://www.pixwox.com/profile/asap.samantha/
  avg_hearts: 200.03
  sorted_time_posted: ["8 hours ago", "2 days ago", "3 days ago", "3 days ago", "4 days ago", "5 days ago", "5 days ago", ...(truncated)
  url: https://www.instagram.com/asap.samantha/
  followers: 98400
  following: 1704
  avg_engagement_c: 0.47
  fullname: Samantha Blender
  avg_comments_c: 260.42
  last_activity_datetime: 2024-05-20T16:14:19.874800000
  creator_gender: female
  username: @asap.samantha
Score: 8.000
```

Node 5:
```
Node ID: @addict_to_beauty_
Text: ["", "✨ Bake it ‘til you make it! ✨ Say hello to flawless skin with Huda Beauty’s Easy Bake Loose Powders. Get ready to blur, set, and slay with that no-flashback finish. Selfie-mode unlocked! 📸\nAre you team pink or team peach? Head over to my stories to vote 🍒🌸🍑🧡\n*PR gifted - no obligation to post\n@hudabeauty\n.\n.\n.\n.\n.\n.\n.\n.\n.\n#hudabeauty #hudabeautyobsessions #hudabeautyshop #hudabeautysettingpowder #settingpowder #settingpowders #makeup #BakeAndGlow #explorepage #pinkaesthetic #p...(truncated)
Metadata:
  comments_c: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 98.0]
  avg_comments: 8.17
  hearts_c: [1599.0, 3733.0, 35.7, 790.0, 1848.0, 800.0, 969.0, 614.0, 5314.0, 74.3, 5231.0, 2691.0]
  keys: influencer
  bio: Just a 30 something year old obsessed beauty addict, sharing her passion with the world 🌍 💜
Beauty D...(truncated)
  posts: 1023
  avg_engagement: 4.10
  platform: instagram
  last_activity: 6 days ago
  hearts: [1599.0, 3733.0, 35.7, 790.0, 1848.0, 800.0, 969.0, 614.0, 5314.0, 74.3, 5231.0, 2691.0]
  engagements: [3.3, 7.71, 0.07, 1.63, 3.82, 1.65, 2.0, 1.27, 10.98, 0.15, 10.81, 5.76]
  engagements_c: [3.3, 7.71, 0.07, 1.63, 3.82, 1.65, 2.0, 1.27, 10.98, 0.15, 10.81, 5.76]
  post_thumbnails: ["https://sp1.pixwox.com/p/pt_6825236811521157392925_0_14856224a31e6939b3762e287b744bef.jpg?v/t51.29...(truncated)
  id: 1947
  avg_hearts_c: 1974.92
  comments: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 98.0]
  url_pixwox: https://www.pixwox.com/profile/addict_to_beauty_/
  avg_hearts: 1974.92
  sorted_time_posted: ["6 days ago", "6 days ago", "1 weeks ago", "1 weeks ago", "1 weeks ago", "1 weeks ago", "2 weeks ag...(truncated)
  url: https://www.instagram.com/addict_to_beauty_/
  followers: 48400
  following: 4997
  avg_engagement_c: 4.10
  fullname: Laura Morris
  avg_comments_c: 8.17
  last_activity_datetime: 2024-05-15T00:13:20.958244000
  username: @addict_to_beauty_
Score: 7.000
```

Node 6:
```
Node ID: wenlozano3/
Text: ["LOLLIPOP LIPS🍭💄🫦 @FBWORKERS @maccosmetics @Gus Ch&aacute...", "MAKEUP LATIN GRAMMYS 📸💄🔝 @Yeri MUA @The Latin Recording Acad...", "BOOTY BOOTY @montpantoja Maquillaje y peinado 🖤 #fyp #trend...", "SHOPPING DE LENTES 👓🕶️🛍️💖 @OPTICAAPVI #lentes #shopping #eye...", "GRWM PARA PINK AURA PARTY🌸🎀💖🌸 #pinkaura #keniaos #makeup #gr...", "Haciendo el GLAM para esta campa&ntilde;a🌈💄👏🏻 @Maybellin...", "Hoy me acompa&ntilde;an a trabajar 💄🪄 @Nicol&aacute;...", "✨📸 #blonde #blondehair #outfitideas #blackoutf...(truncated)
Metadata:
  comments_c: [123.0, 3950.0, 291.0, 8.0, 120.0, 89.0, 48.0, 16.0, 11.0, 13.0, 6.0, 23.0, 49.0, 11.0, 9.0, 25.0, 2...(truncated)
  country: MX
  avg_comments: 235.81
  hearts_c: [28800.0, 1750000.0, 276500.0, 858.0, 24450.0, 14690.0, 5460.0, 796.0, 647.0, 1310.0, 416.0, 1540.0,...(truncated)
  keys: ['beauty', 'makeup', 'influencer']
  bio: Wen Lozano @wenlozano3 BEAUTY INFLUENCER 🎀  INSTAGRAM: @WenLozano FACEBOOK: @WenLozano  JOY2ALL
  language: ['en', 'es', 'none']
  avg_engagement: 30.64
  platform: tiktok
  last_activity: 2024-05-26T17:22:03.438392000
  video_urls_tk: ['https://www.tiktok.com/@wenlozano3/video/7328888893942533382/', 'https://www.tiktok.com/@wenlozano3/video/7302259133669969157/', 'https://www.tiktok.com/@wenlozano3/video/7194627229224160517/', 'https://www.tiktok.com/@wenlozano3/video/7362962303718935816/', 'https://www.tiktok.com/@wenlozano3/video/7361639684784573717/', 'https://www.tiktok.com/@wenlozano3/video/7355317484888624390/', 'https://www.tiktok.com/@wenlozano3/video/7354907780211379462/', 'https://www.tiktok.com/@wenlozano3/video/7352009552625224965/', 'https://www.tiktok.com/@wenlozano3/video/7350000961454329093/', 'https://www.tiktok.com/@wenlozano3/video/7349988787927207174/', 'https://www.tiktok.com/@wenlozano3/video/7349983071841619206/', 'https://www.tiktok.com/@wenlozano3/video/7349041931281911045/', 'https://www.tiktok.com/@wenlozano3/video/7349013101192252677/', 'https://www.tiktok.com/@wenlozano3/video/7348953584500854022/', 'https://www.tiktok.com/@wenlozano3/video/7348952634734169349/', 'https://www.tiktok.com/@wenlozano3/video/7348950980001680645/', 'https://www.tiktok.com/@wenlozano3/video/7348934758040145158/', 'https://www.tiktok.com/@wenlozano3/video/7348660475103563014/', 'https://www.tiktok.com/@wenlozano3/video/7348659527023168773/', 'https://www.tiktok.com/@wenlozano3/video/7348653900645403910/', 'https://www.tiktok.com/@wenlozano3/video/7348648989648014597/']
  hearts: [28800.0, 1750000.0, 276500.0, 858.0, 24450.0, 14690.0, 5460.0, 796.0, 647.0, 1310.0, 416.0, 1540.0,...(truncated)
  engagements: [8.68, 526.24, 83.05, 0.26, 7.37, 4.43, 1.65, 0.24, 0.2, 0.4, 0.13, 0.47, 1.75, 0.26, 0.45, 1.78, 0....(truncated)
  engagements_c: [8.68, 526.24, 83.05, 0.26, 7.37, 4.43, 1.65, 0.24, 0.2, 0.4, 0.13, 0.47, 1.75, 0.26, 0.45, 1.78, 0....(truncated)
  id: 80454
  likes: 6200000
  avg_hearts_c: 101871.48
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/e61edf7606a3e4ae991f7268f01d0f4e~c5_720x720.jpeg
  comments: [123.0, 3950.0, 291.0, 8.0, 120.0, 89.0, 48.0, 16.0, 11.0, 13.0, 6.0, 23.0, 49.0, 11.0, 9.0, 25.0, 2...(truncated)
  avg_hearts: 101871.48
  url: https://www.tiktok.com/@wenlozano3/
  followers: 333300
  following: 181
  name: @wenlozano3
  avg_engagement_c: 30.64
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/1221a4d6e74f90ab9523d774f61ba714.jpg?x-expires=1...(truncated)
  avg_comments_c: 235.81
  earnings_post: 262.09-411.85
Score: 6.000
```

**Evaluation Results:**

- Faithfulness: 0.00 (Fail)
  - Explanation: NO
- Relevancy: 0.00
  - Explanation: NO
- Number of Source Nodes: 6
- Query Runtime: 21.25 seconds

### Query 3: list some popular tech reviewers

**Response:**

Some popular tech reviewers include:

1. TechnoStrefa
2. عبدالله الغفيص (@agafes)
3. Antonio (@techthroughtoni)
4. RodolfoVkz (@rodo_vkz)
5. TecnoGeek (@tecnogeek.oficial)
6. WePC (@wepc)
7. productpulse (@product_pulse1)

**Source Nodes:**

Node 1:
```
Node ID: technostrefa/
Text: ["iPhone 15 vs Galaxy S24 #iphone #samsung ", "Zoom w iPhone vs Galaxy #iphone #samsung #zoom", "iPhone vs Galaxy #iphone #samsung", "[wsp&oacute;łpraca płatna TISSOT] To nie jest zwykły zeg...", "To kolejna nienormalna hulajnoga", "Odpowiadanie użytkownikowi @Chicken Ta poduszka ma wbudowany...", "Czy @Dawid Piątkowski wymienia telefon co roku? 🤔", "Na tę aplikację wszyscy czekają", "Ta drukarka wydrukuje dom w 80 godzin ", "Nadal nie rozumiem jak on to zrobił 😳 @Czarek Czaruje ", "Zoom 25x iPh...(truncated)
Metadata:
  comments_c: [4180.0, 61150.0, 17360.0, 15.0, 163.0, 2.0, 289.0, 11.0, 29.0, 35.0, 69.0, 416.0, 5.0, 32.0, 64.0, ...(truncated)
  country: PL
  avg_comments: 3666.61
  hearts_c: [111470.0, 7310000.0, 2910000.0, 590.0, 10350.0, 194.0, 8180.0, 819.0, 1130.0, 2870.0, 1850.0, 66530...(truncated)
  keys: ['technology', 'gadgets', 'reviews']
  bio: TechnoStrefa @technostrefa Zakręceni wokół technologii 📲🎮 🔥 Zobacz to ⤵️
  language: Polish
  avg_engagement: 35.20
  platform: tiktok
  last_activity: 2024-05-01T19:03:14.969706000
  video_urls_tk: ['https://www.tiktok.com/@technostrefa/video/7326896200987249952/', 'https://www.tiktok.com/@technostrefa/video/7251337026962738458/', 'https://www.tiktok.com/@technostrefa/video/7178790471102254342/', 'https://www.tiktok.com/@technostrefa/video/7363991952548826400/', 'https://www.tiktok.com/@technostrefa/video/7363625299180932385/', 'https://www.tiktok.com/@technostrefa/video/7363314925730532640/', 'https://www.tiktok.com/@technostrefa/video/7363248752980741408/', 'https://www.tiktok.com/@technostrefa/video/7362940503148514592/', 'https://www.tiktok.com/@technostrefa/video/7362847720169655584/', 'https://www.tiktok.com/@technostrefa/video/7362521225962327328/', 'https://www.tiktok.com/@technostrefa/video/7362244558169656608/', 'https://www.tiktok.com/@technostrefa/video/7362110286003752224/', 'https://www.tiktok.com/@technostrefa/video/7361900086055439648/', 'https://www.tiktok.com/@technostrefa/video/7361783545511136544/', 'https://www.tiktok.com/@technostrefa/video/7361437955375811872/', 'https://www.tiktok.com/@technostrefa/video/7361063438606503201/', 'https://www.tiktok.com/@technostrefa/video/7360978232813833505/', 'https://www.tiktok.com/@technostrefa/video/7360702746909101344/', 'https://www.tiktok.com/@technostrefa/video/7360635127199829280/', 'https://www.tiktok.com/@technostrefa/video/7360416304613838113/', 'https://www.tiktok.com/@technostrefa/video/7360345584898673952/', 'https://www.tiktok.com/@technostrefa/video/7359654320389852449/', 'https://www.tiktok.com/@technostrefa/video/7359549503562632480/']
  hearts: [111470.0, 7310000.0, 2910000.0, 590.0, 10350.0, 194.0, 8180.0, 819.0, 1130.0, 2870.0, 1850.0, 66530...(truncated)
  engagements: [8.9, 567.01, 225.18, 0.05, 0.81, 0.02, 0.65, 0.06, 0.09, 0.22, 0.15, 5.15, 0.02, 0.12, 0.21, 0.29, ...(truncated)
  engagements_c: [8.9, 567.01, 225.18, 0.05, 0.81, 0.02, 0.65, 0.06, 0.09, 0.22, 0.15, 5.15, 0.02, 0.12, 0.21, 0.29, ...(truncated)
  id: 73592
  likes: 46500000
  avg_hearts_c: 453987.35
  image: https://p16-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-euttp/39a96f9eb241d5ea0580b40c0834f8f0~c5_7...(truncated)
  comments: [4180.0, 61150.0, 17360.0, 15.0, 163.0, 2.0, 289.0, 11.0, 29.0, 35.0, 69.0, 416.0, 5.0, 32.0, 64.0, ...(truncated)
  avg_hearts: 453987.35
  url: https://www.tiktok.com/@technostrefa/
  followers: 1300000
  following: 1
  name: @technostrefa
  avg_engagement_c: 35.20
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/69c31fcf752a609b88560879d446e5e2.jpg?x-expires=1...(truncated)
  avg_comments_c: 3666.61
  earnings_post: 965.19-1516.73
Score: 10.000
```

Node 2:
```
Node ID: agafes/
Text: ["المصافحة الأولى وفتح صندوق ايفون 15 برو ماكس تيتانيوم طبيعي ...", "#disponsori ساعة هواوي الجديدة والأنيقة #HUAWEIWATCHGT4 ⌚️💚...", "&lrm;شاشة جوال قوية مثل جبل طويق 📱😍⛰️ &lrm;اختبار ق...", "لو خيروك بين رينو 11 أو جالكسي A55 ايش تختار ؟ &rlm;كل ا...", "أغرب طريقة دفع ممكن تشوفها في حياتك 💳🇨🇳 الفكرة هنا أنك تدفع ...", "#disponsori تطبيق رهيب للسفر يعطيك شريحة الكترونية eSIM وتفع...", "سماعة سوني الجديدة مع زر ULT 🎧🔥 السماعة الجديدة ULTWEAR شراي...", "أكبر مكنسة روبوت 🤖 🧹 تنفع للمجمعات المغلقة ...(truncated)
Metadata:
  comments_c: [916.0, 278.0, 5100.0, 32.0, 5.0, 0.0, 16.0, 2.0, 4.0, 54.0, 40.0, 17.0, 3.0, 3.0, 88.0, 25.0, 8.0, ...(truncated)
  country: SA
  avg_comments: 301.43
  hearts_c: [41310.0, 10750.0, 120370.0, 471.0, 110.0, 39.0, 103.0, 60.0, 104.0, 576.0, 719.0, 677.0, 50.0, 1230...(truncated)
  keys: ['technology', 'gadgets', 'reviews']
  bio: عبدالله الغفيص @agafes محب للتقنية وأصنع محتوى حولها  🖥  شاهد قناتي على اليوتيوب ( نيوتك ) للمزيد 😍🤍
  language: Arabic
  creator_age: 25-34
  avg_engagement: 5.19
  platform: tiktok
  last_activity: 2024-04-30T21:10:04.689708000
  video_urls_tk: ['https://www.tiktok.com/@agafes/video/7281313539061566721/', 'https://www.tiktok.com/@agafes/video/7283557990597250306/', 'https://www.tiktok.com/@agafes/video/7176296072959036674/', 'https://www.tiktok.com/@agafes/video/7363239332288744720/', 'https://www.tiktok.com/@agafes/video/7361440688124284161/', 'https://www.tiktok.com/@agafes/video/7361014970626100497/', 'https://www.tiktok.com/@agafes/video/7359534117790272784/', 'https://www.tiktok.com/@agafes/video/7358951419912768769/', 'https://www.tiktok.com/@agafes/video/7355497974165720337/', 'https://www.tiktok.com/@agafes/video/7355215834240863505/', 'https://www.tiktok.com/@agafes/video/7354121295870709008/', 'https://www.tiktok.com/@agafes/video/7353947017036532993/', 'https://www.tiktok.com/@agafes/video/7353826962395254033/', 'https://www.tiktok.com/@agafes/video/7353736766110682369/', 'https://www.tiktok.com/@agafes/video/7353360724992822545/', 'https://www.tiktok.com/@agafes/video/7352974255476198673/', 'https://www.tiktok.com/@agafes/video/فتح-صندوق-أجمل-جوال-وأقوى-كاميرا-في-هاتف-متوسط-قريباً-مراجعة-م-7352659428576972033/', 'https://www.tiktok.com/@agafes/video/7352567229210299665/', 'https://www.tiktok.com/@agafes/video/7352181292638686480/', 'https://www.tiktok.com/@agafes/video/7351855518220078352/', 'https://www.tiktok.com/@agafes/video/7351598859140812034/', 'https://www.tiktok.com/@agafes/video/نحيف-جداً-وفيه-لمسات-جميلة-بالتصميم-هذا-هاتف-هواوي-الجديد-نوفا-7350793682729078017/', 'https://www.tiktok.com/@agafes/video/أخيراً-شفت-جهاز-ألعاب-بمواصفات-قوية-وتصميم-أنيق-7349717084898692353/']
  hearts: [41310.0, 10750.0, 120370.0, 471.0, 110.0, 39.0, 103.0, 60.0, 104.0, 576.0, 719.0, 677.0, 50.0, 1230...(truncated)
  engagements: [25.59, 6.68, 76.04, 0.3, 0.07, 0.02, 0.07, 0.04, 0.07, 0.38, 0.46, 0.42, 0.03, 0.75, 1.28, 0.36, 0....(truncated)
  engagements_c: [25.59, 6.68, 76.04, 0.3, 0.07, 0.02, 0.07, 0.04, 0.07, 0.38, 0.46, 0.42, 0.03, 0.75, 1.28, 0.36, 0....(truncated)
  id: 4097
  likes: 1400000
  avg_hearts_c: 8260.78
  image: https://p77-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/c0c8ed50c965ba4b5ed0051eaec1abe9.jpeg
  comments: [916.0, 278.0, 5100.0, 32.0, 5.0, 0.0, 16.0, 2.0, 4.0, 54.0, 40.0, 17.0, 3.0, 3.0, 88.0, 25.0, 8.0, ...(truncated)
  avg_hearts: 8260.78
  url: https://www.tiktok.com/@agafes/
  followers: 165000
  following: 22
  name: @agafes
  avg_engagement_c: 5.19
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/e1ed44105f4240607f773e927a42610b.jpg?x-expires=1...(truncated)
  avg_comments_c: 301.43
  earnings_post: 120.01-188.59
  creator_gender: male
Score: 9.000
```

Node 3:
```
Node ID: techthroughtoni/
Text: ["#techthroughtoni #sunglasses #smartglasses #ampere #amperedu...", "#techthroughtoni #oneui6 #android14 #samsunga14 #a14 #a14and...", "Samsung Galaxy A14 vs Samsung Galaxy A34 #samsunga14 #samsu...", "#techthroughtoni #siemens #retrotech #oldtech #siemenss4powe...", "8849 Tank 3 Pro vs iPhone 14 Pro Max #8849 #tank3pro #14pro...", "#techthroughtoni #samsunggalaxy #s24 #s24plus #samsungshqipe...", "#techthroughtoni #samsunggalaxy #s24 #samsungshqiperi #shqip...", "#techthroughtoni #samsungshqipe...(truncated)
Metadata:
  comments_c: [638.0, 1970.0, 2170.0, 0.0, 16.0, 18.0, 27.0, 10.0, 20.0, 19.0, 20.0, 2.0, 34.0, 351.0, 38.0, 5.0, ...(truncated)
  country: AL
  avg_comments: 238.04
  hearts_c: [41000.0, 96200.0, 116820.0, 80.0, 104.0, 182.0, 324.0, 293.0, 185.0, 228.0, 154.0, 82.0, 309.0, 113...(truncated)
  keys: ['technology', 'gadgets', 'reviews']
  bio: Antonio @techthroughtoni Më gjeni më poshtë / You can find me below  Faleminderit 🙏 / Thanks 🙏 ⬇️ ⬇️
  language: Albanian
  avg_engagement: 11.06
  platform: tiktok
  last_activity: 2024-04-30T20:55:05.081499000
  video_urls_tk: ['https://www.tiktok.com/@techthroughtoni/video/7348753179951074566/', 'https://www.tiktok.com/@techthroughtoni/video/7315980462592150790/', 'https://www.tiktok.com/@techthroughtoni/video/7245690496553684230/', 'https://www.tiktok.com/@techthroughtoni/video/7363397941106625797/', 'https://www.tiktok.com/@techthroughtoni/video/7362888541543681286/', 'https://www.tiktok.com/@techthroughtoni/video/7361336946183900422/', 'https://www.tiktok.com/@techthroughtoni/video/7360826358710144262/', 'https://www.tiktok.com/@techthroughtoni/video/7360666603060481286/', 'https://www.tiktok.com/@techthroughtoni/video/7359987451965852934/', 'https://www.tiktok.com/@techthroughtoni/video/7359661225652882693/', 'https://www.tiktok.com/@techthroughtoni/video/7359522501245832453/', 'https://www.tiktok.com/@techthroughtoni/video/7359150251577527557/', 'https://www.tiktok.com/@techthroughtoni/video/7358034285418319109/', 'https://www.tiktok.com/@techthroughtoni/video/7356336009115684102/', 'https://www.tiktok.com/@techthroughtoni/video/7355767275183443205/', 'https://www.tiktok.com/@techthroughtoni/video/7355604286640082182/', 'https://www.tiktok.com/@techthroughtoni/video/7355479082173271301/', 'https://www.tiktok.com/@techthroughtoni/video/7355211113849490693/', 'https://www.tiktok.com/@techthroughtoni/video/7355204707549302021/', 'https://www.tiktok.com/@techthroughtoni/video/7355169580567809286/', 'https://www.tiktok.com/@techthroughtoni/video/7354819669150403845/', 'https://www.tiktok.com/@techthroughtoni/video/7354750597205101830/', 'https://www.tiktok.com/@techthroughtoni/video/7354709795129085189/']
  hearts: [41000.0, 96200.0, 116820.0, 80.0, 104.0, 182.0, 324.0, 293.0, 185.0, 228.0, 154.0, 82.0, 309.0, 113...(truncated)
  engagements: [38.38, 90.48, 109.67, 0.07, 0.11, 0.18, 0.32, 0.28, 0.19, 0.23, 0.16, 0.08, 0.32, 10.78, 0.58, 0.16...(truncated)
  engagements_c: [38.38, 90.48, 109.67, 0.07, 0.11, 0.18, 0.32, 0.28, 0.19, 0.23, 0.16, 0.08, 0.32, 10.78, 0.58, 0.16...(truncated)
  id: 73603
  likes: 3000000
  avg_hearts_c: 11757.17
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/51f93d545398298045f2309133a07de1~c5_720x720.jpeg
  comments: [638.0, 1970.0, 2170.0, 0.0, 16.0, 18.0, 27.0, 10.0, 20.0, 19.0, 20.0, 2.0, 34.0, 351.0, 38.0, 5.0, ...(truncated)
  avg_hearts: 11757.17
  url: https://www.tiktok.com/@techthroughtoni/
  followers: 108500
  following: 70
  name: @techthroughtoni
  avg_engagement_c: 11.06
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/a061aea9ced5435430fde87474d0e2a3.jpg?x-expires=1...(truncated)
  avg_comments_c: 238.04
  earnings_post: 86.42-135.81
Score: 8.000
```

Node 4:
```
Node ID: 3d5a453a-01dc-4a8d-823f-1e1c8291f209
Text: The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@apple_tech_journal', 'BELONGS_TO', 'instagram_"desksetup"\n"StarWars"')
('@geeky.techie', 'BELONGS_TO', 'instagram_1.Tech\n2.Gadgets\n3.Reviewer')
('@apple_tech_journal', 'BELONGS_TO', 'instagram_"hightech"\n"retro"')
('nanotekcomputersolutions/', 'BELONGS_TO', 'tiktok_computers')
('geekbuyingofficial/', 'BELONGS_TO', 'tiktok_te...(truncated)
Metadata:
  kg_rel_texts: ['(\'@apple_tech_journal\', \'BELONGS_TO\', \'instagram_"desksetup"\\n"StarWars"\')', "('@geeky.techie', 'BELONGS_TO', 'instagram_1.Tech\\n2.Gadgets\\n3.Reviewer')", '(\'@apple_tech_journal\', \'BELONGS_TO\', \'instagram_"hightech"\\n"retro"\')', "('nanotekcomputersolutions/', 'BELONGS_TO', 'tiktok_computers')", "('geekbuyingofficial/', 'BELONGS_TO', 'tiktok_techreviews')", "('@falarafa_tech', 'BELONGS_TO', 'instagram_tech_reviewer')", "('mahran.review.9295/', 'BELONGS_TO', 'tiktok_technology')", "('popularmechanics/', 'BELONGS_TO', 'tiktok_technology')", "('reviewsen60segundos/', 'BELONGS_TO', 'tiktok_gaming')", "('lestripezyt/', 'BELONGS_TO', 'tiktok_tech reviews')", "('talha_reviews/', 'BELONGS_TO', 'tiktok_technology')", "('@gadgets_reviews0', 'BELONGS_TO', 'instagram_tech')", "('techthroughtoni/', 'BELONGS_TO', 'tiktok_reviews')", "('@era_of_tech', 'BELONGS_TO', 'instagram_StarWars')", "('thetechyoutuber/', 'BELONGS_TO', 'tiktok_gadgets')", "('@reviewingtech', 'BELONGS_TO', 'instagram_tech')", "('thetechyoutuber/', 'BELONGS_TO', 'tiktok_tech')", "('technostrefa/', 'BELONGS_TO', 'tiktok_reviews')", "('thetechboy_/', 'BELONGS_TO', 'tiktok_gadgets')", "('geekynews/', 'BELONGS_TO', 'tiktok_robotics')", "('geekynews/', 'BELONGS_TO', 'tiktok_technews')", "('mr.mxtech/', 'BELONGS_TO', 'tiktok_reviews')", "('bizutech/', 'BELONGS_TO', 'tiktok_reviews')", "('mmtrtech/', 'BELONGS_TO', 'tiktok_reviews')", "('thetechboy_/', 'BELONGS_TO', 'tiktok_tech')"]
  kg_rel_map: {'tech': [], 'popular': [], 'reviewers': []}
Score: 8.000
```

Node 5:
```
Node ID: rodo_vkz/
Text: ["Teclado y mouse por 15 pesos?! 🤯 C&oacute;digo: dkj7248...", "No compres el iphone 11 en 2022 #iphonetricks #apple #iphone...", "Adios iphone x tw ira mejor en el empe&ntilde;o 🥺😩 #ios ...", "Adios tiktok #tiktok #iphone ", "Mo tires tu ipad ojo #apple #iphone #ipad ", "Samsung 🤡 #iphone #android #apple ", "Bloquearon WhatsApp 🤯 #ios # #iphone ", "Adios disney plus 😔", "Adios windows 10 🕊️🕊️🕊️#windows #pcgaming ", "Le ganaron al iphone 🤯 #apple #iphone ", "Canciones ia #apple #iphone #tikring...(truncated)
Metadata:
  comments_c: [995.0, 9970.0, 13290.0, 3.0, 30.0, 52.0, 47.0, 550.0, 2100.0, 938.0, 6.0, 473.0, 275.0, 85.0, 158.0...(truncated)
  country: MX
  avg_comments: 1348.65
  hearts_c: [229310.0, 886540.0, 918230.0, 196.0, 10910.0, 4960.0, 3240.0, 52990.0, 44720.0, 84560.0, 199.0, 129...(truncated)
  keys: ['technology', 'gadgets', 'reviews']
  bio: RodolfoVkz •Te Sigue @rodo_vkz ✉️Rodolfo.vazquezmoreno@viep.com.mx✉️ TEMU: dkx2293 ⬇️ compra tu iPho...(truncated)
  language: ['es', 'en', 'none']
  avg_engagement: 40.79
  platform: tiktok
  last_activity: 2024-05-28T04:23:26.927422000
  video_urls_tk: ['https://www.tiktok.com/@rodo_vkz/video/7316561621751450886/', 'https://www.tiktok.com/@rodo_vkz/video/7118494357384170757/', 'https://www.tiktok.com/@rodo_vkz/video/7218667032630299910/', 'https://www.tiktok.com/@rodo_vkz/video/7363822839658581256/', 'https://www.tiktok.com/@rodo_vkz/video/7361532922123324679/', 'https://www.tiktok.com/@rodo_vkz/video/7360810281913650437/', 'https://www.tiktok.com/@rodo_vkz/video/7360014782407216390/', 'https://www.tiktok.com/@rodo_vkz/video/7358567185163275526/', 'https://www.tiktok.com/@rodo_vkz/video/7357838142432365830/', 'https://www.tiktok.com/@rodo_vkz/video/7356387242287435014/', 'https://www.tiktok.com/@rodo_vkz/video/7355234000622931205/', 'https://www.tiktok.com/@rodo_vkz/video/7354818050652146950/', 'https://www.tiktok.com/@rodo_vkz/video/7353703210596584710/', 'https://www.tiktok.com/@rodo_vkz/video/7352602652997324037/', 'https://www.tiktok.com/@rodo_vkz/video/7352199409175661829/', 'https://www.tiktok.com/@rodo_vkz/video/7351879207074450694/', 'https://www.tiktok.com/@rodo_vkz/video/7351516433190259973/', 'https://www.tiktok.com/@rodo_vkz/video/7351429696132877574/', 'https://www.tiktok.com/@rodo_vkz/video/7350816079108656390/', 'https://www.tiktok.com/@rodo_vkz/video/7350327313822682373/', 'https://www.tiktok.com/@rodo_vkz/video/7350004141818793221/', 'https://www.tiktok.com/@rodo_vkz/video/7349294094776159494/', 'https://www.tiktok.com/@rodo_vkz/video/7347788868072049925/']
  hearts: [229310.0, 886540.0, 918230.0, 196.0, 10910.0, 4960.0, 3240.0, 52990.0, 44720.0, 84560.0, 199.0, 129...(truncated)
  engagements: [74.63, 290.51, 301.85, 0.06, 3.55, 1.62, 1.07, 17.35, 15.17, 27.71, 0.07, 4.34, 29.5, 4.19, 3.94, 3...(truncated)
  engagements_c: [74.63, 290.51, 301.85, 0.06, 3.55, 1.62, 1.07, 17.35, 15.17, 27.71, 0.07, 4.34, 29.5, 4.19, 3.94, 3...(truncated)
  id: 64670
  likes: 12300000
  avg_hearts_c: 124518.96
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/5e3fc59d41f36efbbb82e639bf852f42~c5_720x720.jpeg
  comments: [995.0, 9970.0, 13290.0, 3.0, 30.0, 52.0, 47.0, 550.0, 2100.0, 938.0, 6.0, 473.0, 275.0, 85.0, 158.0...(truncated)
  avg_hearts: 124518.96
  url: https://www.tiktok.com/@rodo_vkz/
  followers: 308600
  following: 99
  name: @rodo_vkz
  avg_engagement_c: 40.79
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/c6ebd67b0b73d2d4b4025b7b5b3d260c.jpg?x-expires=1...(truncated)
  avg_comments_c: 1348.65
  earnings_post: 249.32-391.79
Score: 7.000
```

Node 6:
```
Node ID: tecnogeek.oficial/
Text: ["O melhor Tablet custo benef&iacute;cio at&eacute; mi...", "Celular indestrut&iacute;vel super resistente e tamb&amp...", "Comprei um SSD de 30 reais no Aliexpress! . Esse &eacute...", "Comprei um celular indestrut&iacute;vel 😎👍 ➡️ O link do ...", "Melhores Celulares Baratos que o pre&ccedil;o caiu e val...", "Celulares Exclusivos que ningu&eacute;m tem no Brasil 😎👍...", "Esse &eacute; melhor gamepad para celular com o melhor c...", "Como melhorar a c&acirc;mera do iPhone e fazer ela virar...",...(truncated)
Metadata:
  comments_c: [1470.0, 6270.0, 728.0, 668.0, 151.0, 39.0, 24.0, 39.0, 6.0, 867.0, 4.0, 30.0, 140.0, 191.0, 69.0, 1...(truncated)
  country: BR
  avg_comments: 666.68
  hearts_c: [170040.0, 374550.0, 80580.0, 28230.0, 23030.0, 7130.0, 3490.0, 3660.0, 1300.0, 76150.0, 662.0, 4690...(truncated)
  keys: ['technology', 'gadgets', 'reviews']
  bio: TecnoGeek @tecnogeek.oficial 🌐 Dicas de Tecnologia (Se o link não aparecer, tá no meu Instagram) ⤵️L...(truncated)
  language: Portuguese
  creator_age: 25-34
  avg_engagement: 12.32
  platform: tiktok
  last_activity: 2024-04-17T21:10:09.063211000
  video_urls_tk: ['https://www.tiktok.com/@tecnogeek.oficial/video/7311794653076966662/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7325419441154477317/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7233920048954363142/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7358128925882600710/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7355645298208787717/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7355229359784873222/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7353690333416328453/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7351942997308738822/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7349982281764752645/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7348911467271441669/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7348485715493195014/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7347508190705241349/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7345256071545638150/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7342963414345714950/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7341911543061171461/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7341560459784473862/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7340360670891756805/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7336216987338689798/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7335610791325928710/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7335161927330499846/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7334808007420726534/', 'https://www.tiktok.com/@tecnogeek.oficial/video/7334095602097130757/']
  hearts: [170040.0, 374550.0, 80580.0, 28230.0, 23030.0, 7130.0, 3490.0, 3660.0, 1300.0, 76150.0, 662.0, 4690...(truncated)
  engagements: [42.92, 95.3, 20.35, 7.23, 5.8, 1.79, 0.88, 0.93, 0.33, 19.27, 0.17, 1.18, 6.21, 3.66, 1.13, 0.49, 7...(truncated)
  engagements_c: [42.92, 95.3, 20.35, 7.23, 5.8, 1.79, 0.88, 0.93, 0.33, 19.27, 0.17, 1.18, 6.21, 3.66, 1.13, 0.49, 7...(truncated)
  id: 73611
  likes: 6800000
  avg_hearts_c: 48556.91
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/39e6027d728324f889ca9a28d172fcab~c5_720x720.jpeg
  comments: [1470.0, 6270.0, 728.0, 668.0, 151.0, 39.0, 24.0, 39.0, 6.0, 867.0, 4.0, 30.0, 140.0, 191.0, 69.0, 1...(truncated)
  avg_hearts: 48556.91
  url: https://www.tiktok.com/@tecnogeek.oficial/
  followers: 399600
  following: 83
  name: @tecnogeek.oficial
  avg_engagement_c: 12.32
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/d50084519a79235fe25f40d34a97c0f4.jpg?x-expires=1...(truncated)
  avg_comments_c: 666.68
  earnings_post: 302.69-475.66
  creator_gender: male
Score: 6.000
```

Node 7:
```
Node ID: wepc/
Text: ["Hogwarts Legacy Graphics VS PS1 #hogwartslegacy #ps1harrypo...", "RTX 4090 In a mini ITX motherboard?#rtx4090 #4090 #miniitx #...", "We&rsquo;ve put Monitor Refresh Rates to the test! ⚡️ - ...", "What&#039;s The Difference Between DLSS and FSR2? #dlss ...", "A subtle and powerful prebuilt From ASUS! #asus #proart #po...", "Overkill Or Awesome? That&#039;s the real question ❓⁉️ ...", "F1 24 RTX 3080Ti, High Settings, Resolution Comparison 🏎️ #f...", "What is your opinion on game key retailers? ...(truncated)
Metadata:
  comments_c: [4810.0, 5200.0, 4540.0, 18.0, 4.0, 10.0, 13.0, 3.0, 13.0, 1.0, 3.0, 31.0, 6.0, 3.0, 5.0, 61.0, 7.0,...(truncated)
  country: GB
  avg_comments: 646.00
  hearts_c: [430090.0, 615210.0, 272570.0, 86.0, 83.0, 81.0, 279.0, 61.0, 134.0, 169.0, 91.0, 424.0, 265.0, 65.0...(truncated)
  keys: ['gaming', 'technology', 'reviews']
  bio: WePC @wepc 🎮 PC Gaming Tech 🎮 —————— Builds, Tests, & Reviews!
  language: ['en', 'none', 'none']
  avg_engagement: 13.21
  platform: tiktok
  last_activity: 2024-06-09T02:00:29.845727000
  video_urls_tk: ['https://www.tiktok.com/@wepc/video/7198131272093404422/', 'https://www.tiktok.com/@wepc/video/7154400768609488134/', 'https://www.tiktok.com/@wepc/video/6974797072843230469/', 'https://www.tiktok.com/@wepc/video/7375904092754840864/', 'https://www.tiktok.com/@wepc/video/7375560026762562849/', 'https://www.tiktok.com/@wepc/video/7375199370179906848/', 'https://www.tiktok.com/@wepc/video/7375102502825364768/', 'https://www.tiktok.com/@wepc/video/7374896685647973665/', 'https://www.tiktok.com/@wepc/video/7374444635613285665/', 'https://www.tiktok.com/@wepc/video/7374115194210929952/', 'https://www.tiktok.com/@wepc/video/7374032044998888736/', 'https://www.tiktok.com/@wepc/video/7373659488571739425/', 'https://www.tiktok.com/@wepc/video/7373395096030448929/', 'https://www.tiktok.com/@wepc/video/7373271428147219744/', 'https://www.tiktok.com/@wepc/video/7372891149691833632/', 'https://www.tiktok.com/@wepc/video/7372614692168011040/', 'https://www.tiktok.com/@wepc/video/7372572173610896672/', 'https://www.tiktok.com/@wepc/video/7372291366581210400/', 'https://www.tiktok.com/@wepc/video/7372137784452058400/', 'https://www.tiktok.com/@wepc/video/7371866601567702305/', 'https://www.tiktok.com/@wepc/video/7371488401129737504/', 'https://www.tiktok.com/@wepc/video/7371098061973540128/', 'https://www.tiktok.com/@wepc/video/7370798188627807520/']
  hearts: [430090.0, 615210.0, 272570.0, 86.0, 83.0, 81.0, 279.0, 61.0, 134.0, 169.0, 91.0, 424.0, 265.0, 65.0...(truncated)
  engagements: [98.84, 141.0, 62.98, 0.02, 0.02, 0.02, 0.07, 0.01, 0.03, 0.04, 0.02, 0.1, 0.06, 0.02, 0.05, 0.09, 0...(truncated)
  engagements_c: [98.84, 141.0, 62.98, 0.02, 0.02, 0.02, 0.07, 0.01, 0.03, 0.04, 0.02, 0.1, 0.06, 0.02, 0.05, 0.09, 0...(truncated)
  id: 80460
  likes: 10200000
  avg_hearts_c: 57480.78
  image: https://p77-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/cb0c9da97bef1828c040664dd3c0e6bc.jpeg
  comments: [4810.0, 5200.0, 4540.0, 18.0, 4.0, 10.0, 13.0, 3.0, 13.0, 1.0, 3.0, 31.0, 6.0, 3.0, 5.0, 61.0, 7.0,...(truncated)
  avg_hearts: 57480.78
  url: https://www.tiktok.com/@wepc/
  followers: 440000
  following: 105
  name: @wepc
  avg_engagement_c: 13.21
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/3b6ae0355957173ae510c0718a8984c2.jpg?x-expires=1...(truncated)
  avg_comments_c: 646.00
  earnings_post: 322.06-506.09
Score: 5.000
```

Node 8:
```
Node ID: product_pulse1/
Text: ["It&#039;s so special, it&#039;s much safer to wear e...", "eGPU for Laptop/Laptop Name: GPD WIN MAX #Unboxing #Shorts #...", "smart pen🥱🤯🤯 #Technology #Smartphones #TechNews #FutureTech ...", "❤️😍🫂 #amazonfinds #amazonmusthaves #amazon #amazongadgets #f...", "❤️😍🫂 #amazonfinds #amazonmusthaves #amazon #amazongadgets #f...", "❤️😍🫂 #amazonfinds #amazonmusthaves #amazon #amazongadgets #f...", "❤️😍🫂 #amazonfinds #amazonmusthaves #amazon #amazongadgets #f...", "❤️😍🫂 #amazonfinds #amazonmusthaves #a...(truncated)
Metadata:
  comments_c: [0.0, 1280.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0...(truncated)
  country: MA
  avg_comments: 55.91
  hearts_c: [7140.0, 75470.0, 10380.0, 7.0, 79.0, 5.0, 3.0, 5.0, 3.0, 2.0, 5.0, 7.0, 75.0, 4.0, 5.0, 15.0, 11.0,...(truncated)
  keys: ['reviews', 'technology', 'gadgets']
  bio: productpulse @product_pulse1 Product Pulse: Your go-to for trustworthy product reviews."
  language: English
  creator_age: 25-34
  avg_engagement: 35.13
  platform: tiktok
  last_activity: 2024-04-28T21:13:12.919804000
  video_urls_tk: ['https://www.tiktok.com/@product_pulse1/video/7262132427374497029/', 'https://www.tiktok.com/@product_pulse1/video/7324367650447052037/', 'https://www.tiktok.com/@product_pulse1/video/7261306159867383045/', 'https://www.tiktok.com/@product_pulse1/video/7362758843996081414/', 'https://www.tiktok.com/@product_pulse1/video/7362758752396758278/', 'https://www.tiktok.com/@product_pulse1/video/7362673396292783366/', 'https://www.tiktok.com/@product_pulse1/video/7362673114234342661/', 'https://www.tiktok.com/@product_pulse1/video/7362672709521788165/', 'https://www.tiktok.com/@product_pulse1/video/7362255737650826501/', 'https://www.tiktok.com/@product_pulse1/video/7362255636349963526/', 'https://www.tiktok.com/@product_pulse1/video/7361446596770368774/', 'https://www.tiktok.com/@product_pulse1/video/7361446414288768262/', 'https://www.tiktok.com/@product_pulse1/video/7361446078660496646/', 'https://www.tiktok.com/@product_pulse1/video/7360691822227721478/', 'https://www.tiktok.com/@product_pulse1/video/7360325101360778502/', 'https://www.tiktok.com/@product_pulse1/video/7360324853859093765/', 'https://www.tiktok.com/@product_pulse1/video/7360324677601955077/', 'https://www.tiktok.com/@product_pulse1/video/7360324405106363654/', 'https://www.tiktok.com/@product_pulse1/video/7360322970994363653/', 'https://www.tiktok.com/@product_pulse1/video/7360322353374448901/', 'https://www.tiktok.com/@product_pulse1/video/7359697497196989702/', 'https://www.tiktok.com/@product_pulse1/video/7359696856869391622/', 'https://www.tiktok.com/@product_pulse1/video/7359695029725678853/']
  hearts: [7140.0, 75470.0, 10380.0, 7.0, 79.0, 5.0, 3.0, 5.0, 3.0, 2.0, 5.0, 7.0, 75.0, 4.0, 5.0, 15.0, 11.0,...(truncated)
  engagements: [61.03, 655.98, 88.74, 0.06, 0.68, 0.04, 0.03, 0.04, 0.03, 0.03, 0.04, 0.07, 0.65, 0.03, 0.04, 0.13,...(truncated)
  engagements_c: [61.03, 655.98, 88.74, 0.06, 0.68, 0.04, 0.03, 0.04, 0.03, 0.03, 0.04, 0.07, 0.65, 0.03, 0.04, 0.13,...(truncated)
  id: 61468
  likes: 116300
  avg_hearts_c: 4054.09
  image: https://p77-va.tiktokcdn.com/tos-maliva-avt-0068/e2cb8eb435fdde85fc2a67fe50935553~c5_720x720.jpeg
  comments: [0.0, 1280.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0...(truncated)
  avg_hearts: 4054.09
  url: https://www.tiktok.com/@product_pulse1/
  followers: 11700
  following: 78
  name: @product_pulse1
  avg_engagement_c: 35.13
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/71877be032bc14bacbfa6aa9b0a18c19.jpg?x-expires=1...(truncated)
  avg_comments_c: 55.91
  earnings_post: 8.32-13.08
  creator_gender: female
Score: 4.000
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 1.00
  - Explanation: YES
- Number of Source Nodes: 8
- Query Runtime: 941.67 seconds

### Query 4: what are the trending fashion channels?

**Response:**

The trending fashion channels include:

1. @fashionbymomoyo on Instagram
2. @hour_glass_couture on Instagram
3. @blouse_designs.on_trend on Instagram
4. @trendboutiquemiami on Instagram
5. @trend_setter_shop on Instagram
6. @runway_channel on Instagram
7. @trendeminence on Instagram
8. trendingwithkennedi on TikTok
9. culturalstyleweek on TikTok
10. trendsetters1459 on TikTok
11. fashionmagazine on TikTok
12. trend.store.dz on TikTok
13. trends0199 on TikTok
14. trendz91 on TikTok
15. footwearnews on TikTok
16. trendkidds on TikTok

**Source Nodes:**

Node 1:
```
Node ID: 009129d3-06c7-4bd6-b2bf-6de2851e158f
Text: The following are knowledge sequence in max depth 2 in the form of directed graph like:
`subject -[predicate]->, object, <-[predicate_next_hop]-, object_next_hop ...`
('@fashionbymomoyo', 'BELONGS_TO', "instagram_'inspiration'\n'trendy'")
('@hour_glass_couture', 'BELONGS_TO', 'instagram_trendy fashion')
('@blouse_designs.on_trend', 'BELONGS_TO', 'instagram_fashion')
('@trendboutiquemiami', 'BELONGS_TO', 'instagram_fashion')
('@trend_setter_shop', 'BELONGS_TO', 'instagram_fashion')
('trendingwith...(truncated)
Metadata:
  kg_rel_texts: ['(\'@fashionbymomoyo\', \'BELONGS_TO\', "instagram_\'inspiration\'\\n\'trendy\'")', "('@hour_glass_couture', 'BELONGS_TO', 'instagram_trendy fashion')", "('@blouse_designs.on_trend', 'BELONGS_TO', 'instagram_fashion')", "('@trendboutiquemiami', 'BELONGS_TO', 'instagram_fashion')", "('@trend_setter_shop', 'BELONGS_TO', 'instagram_fashion')", "('trendingwithkennedi/', 'BELONGS_TO', 'tiktok_fashion')", "('fashionnprodigy/', 'BELONGS_TO', 'tiktok_trendsetter')", "('trendingwithkennedi/', 'BELONGS_TO', 'tiktok_beauty')", "('@runway_channel', 'BELONGS_TO', 'instagram_fashion')", "('culturalstyleweek/', 'BELONGS_TO', 'tiktok_fashion')", "('trendingcrockery01/', 'BELONGS_TO', 'tiktok_brands')", "('trendwatcher23/', 'BELONGS_TO', 'tiktok_curiosity')", "('trendsetters1459/', 'BELONGS_TO', 'tiktok_fashion')", "('@trendeminence', 'BELONGS_TO', 'instagram_fashion')", "('trendymakeoverss/', 'BELONGS_TO', 'tiktok_makeup')", "('fashionmagazine/', 'BELONGS_TO', 'tiktok_fashion')", "('trend.store.dz/', 'BELONGS_TO', 'tiktok_fashion')", "('trendygabriel/', 'BELONGS_TO', 'tiktok_jewelry')", "('trendymakeoverss/', 'BELONGS_TO', 'tiktok_glam')", "('trendywanderer/', 'BELONGS_TO', 'tiktok_luxury')", "('footwearnews/', 'BELONGS_TO', 'tiktok_fashion')", "('trendkidds/', 'BELONGS_TO', 'tiktok_fashion')", "('trendy246/', 'BELONGS_TO', 'tiktok_trendies')", "('trends0199/', 'BELONGS_TO', 'tiktok_fashion')", "('trendz91/', 'BELONGS_TO', 'tiktok_fashion')"]
  kg_rel_map: {'fashion': [], 'channels': [], 'trending': []}
Score: 10.000
```

Node 2:
```
Node ID: dollfitz/
Text: ["they&rsquo;re sooooo cute and comfy! #fyp #aerie #longsl...", "it saved my straight lashes! #fyp #underratedmakeup #maybell...", "the way this series is the only thing keeping my acct alive ...", "can u believe i got the calico critter set for $5??? #fyp #n...", "haul coming soon :) #fyp #nyc #city #museum #brandymelville ...", "i wish i had her swag #fyp #metmuseum #nyc #myseum #sculptur...", "blush is so fun its my favorite &gt;.&lt; #fyp #blus...", "thank you at @YesStyle @YesStyleInfluence...(truncated)
Metadata:
  comments_c: [832.0, 1480.0, 1170.0, 14.0, 2.0, 2.0, 2.0, 0.0, 8.0, 0.0, 3.0, 10.0, 8.0, 2.0, 4.0, 7.0, 0.0, 5.0,...(truncated)
  country: US
  avg_comments: 156.78
  hearts_c: [473050.0, 452540.0, 400490.0, 801.0, 114.0, 330.0, 963.0, 259.0, 293.0, 111.0, 74.0, 1260.0, 1430.0...(truncated)
  keys: ['fashion', 'beauty', 'makeup']
  bio: syd <3 @dollfitz 18 lover of pretty things 💌 dollfitz05@gmail.com
  language: English
  creator_age: 18-24
  avg_engagement: 114.02
  platform: tiktok
  last_activity: 2024-05-28T06:23:07.042410000
  video_urls_tk: ['https://www.tiktok.com/@dollfitz/video/7168150944444681514/', 'https://www.tiktok.com/@dollfitz/video/7184460344524361003/', 'https://www.tiktok.com/@dollfitz/video/7204950310236720426/', 'https://www.tiktok.com/@dollfitz/video/7363762735374404907/', 'https://www.tiktok.com/@dollfitz/video/7363401619922292010/', 'https://www.tiktok.com/@dollfitz/video/7362996509136293166/', 'https://www.tiktok.com/@dollfitz/video/7361905365048462635/', 'https://www.tiktok.com/@dollfitz/video/7360075206599167274/', 'https://www.tiktok.com/@dollfitz/video/7359654617547935019/', 'https://www.tiktok.com/@dollfitz/video/7359645565304507694/', 'https://www.tiktok.com/@dollfitz/video/7359308620825365806/', 'https://www.tiktok.com/@dollfitz/video/7357399170975616298/', 'https://www.tiktok.com/@dollfitz/video/7357393383226117419/', 'https://www.tiktok.com/@dollfitz/video/7353694282919873838/', 'https://www.tiktok.com/@dollfitz/video/7353692234115517739/', 'https://www.tiktok.com/@dollfitz/video/7352026210572012842/', 'https://www.tiktok.com/@dollfitz/video/7351886865223486762/', 'https://www.tiktok.com/@dollfitz/video/7351883483104415018/', 'https://www.tiktok.com/@dollfitz/video/7351870975010606382/', 'https://www.tiktok.com/@dollfitz/video/7351280239483292971/', 'https://www.tiktok.com/@dollfitz/video/7349405548120476971/', 'https://www.tiktok.com/@dollfitz/video/7349294585559977258/', 'https://www.tiktok.com/@dollfitz/video/7348166071377087786/']
  hearts: [473050.0, 452540.0, 400490.0, 801.0, 114.0, 330.0, 963.0, 259.0, 293.0, 111.0, 74.0, 1260.0, 1430.0...(truncated)
  engagements: [913.07, 874.8, 773.91, 1.57, 0.22, 0.64, 1.86, 0.5, 0.58, 0.21, 0.15, 2.45, 2.77, 0.24, 3.21, 2.56,...(truncated)
  engagements_c: [913.07, 874.8, 773.91, 1.57, 0.22, 0.64, 1.86, 0.5, 0.58, 0.21, 0.15, 2.45, 2.77, 0.24, 3.21, 2.56,...(truncated)
  id: 21754
  likes: 8100000
  avg_hearts_c: 59021.22
  image: https://p19-pu-useast8.tiktokcdn-us.com/tos-useast5-avt-0068-tx/cce8e0e1c0fe44742afae2f96df13fac~c5_...(truncated)
  comments: [832.0, 1480.0, 1170.0, 14.0, 2.0, 2.0, 2.0, 0.0, 8.0, 0.0, 3.0, 10.0, 8.0, 2.0, 4.0, 7.0, 0.0, 5.0,...(truncated)
  avg_hearts: 59021.22
  url: https://www.tiktok.com/@dollfitz/
  followers: 51900
  following: 301
  name: @dollfitz
  avg_engagement_c: 114.02
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/9f2f05e070ba657f28eb040d3ce828f7.jpg?x-expires=1...(truncated)
  avg_comments_c: 156.78
  earnings_post: 43.32-68.07
  creator_gender: female
Score: 9.000
```

Node 3:
```
Node ID: myageorgie/
Text: ["@Storyjewellery #mothersdaygiftideas2024 #storyjewellery #wi...", "PSD #fyp #foryoupage #trending #tryonhaul ", "#fyp #hardwork #God ", "#fyp #foryoupage #God ", "#fyp ", "#foryoupage #fyp #trending #God", "Black Cherry Pomegranate is soooo gooood! Get yours at @Doll...", "#foryourpage #trending #God #lifesbetter ", "#foryourpage #fyp #trending #maturing ", "#fyp #God #foryourpage #deserve ", "#foryoupage #God #kissing ", "core memory #paris #eiffeltower #track #athlete #athletics #...", "@Des...(truncated)
Metadata:
  comments_c: [0.0, 1.0, 174.0, 99.0, 77.0, 11.0, 0.0, 9.0, 4.0, 26.0, 17.0, 14.0, 1.0, 1.0, 14.0, 13.0]
  country: US
  avg_comments: 28.81
  hearts_c: [479.0, 107.0, 79100.0, 72120.0, 16110.0, 8470.0, 54.0, 1690.0, 2920.0, 10950.0, 2370.0, 2990.0, 192...(truncated)
  keys: ['jewelry', 'fashion', 'beauty']
  bio: Mya Γεωργιάδου @myageorgie urfavvandygirl insta-myageorgie 👻-myageorgiadis 💌 -mya.georgiadis@icloud....(truncated)
  language: Greek
  creator_age: 20-24
  avg_engagement: 37.62
  platform: tiktok
  last_activity: 2024-04-24T20:56:30.646665000
  video_urls_tk: ['https://www.tiktok.com/@myageorgie/video/7360900350888611115/', 'https://www.tiktok.com/@myageorgie/video/7360062274306084142/', 'https://www.tiktok.com/@myageorgie/video/7357713114894437678/', 'https://www.tiktok.com/@myageorgie/video/7357711529011121451/', 'https://www.tiktok.com/@myageorgie/video/7357595962740657451/', 'https://www.tiktok.com/@myageorgie/video/7354089851093880106/', 'https://www.tiktok.com/@myageorgie/video/7354081542148197675/', 'https://www.tiktok.com/@myageorgie/video/7353494532714941738/', 'https://www.tiktok.com/@myageorgie/video/7352312349518335274/', 'https://www.tiktok.com/@myageorgie/video/7347672192852790571/', 'https://www.tiktok.com/@myageorgie/video/7346637727376493866/', 'https://www.tiktok.com/@myageorgie/video/7346355773615738154/', 'https://www.tiktok.com/@myageorgie/video/7335162967496985898/', 'https://www.tiktok.com/@myageorgie/video/7335161967641988395/', 'https://www.tiktok.com/@myageorgie/video/7331832012505926954/', 'https://www.tiktok.com/@myageorgie/video/7328556748950867246/']
  hearts: [479.0, 107.0, 79100.0, 72120.0, 16110.0, 8470.0, 54.0, 1690.0, 2920.0, 10950.0, 2370.0, 2990.0, 192...(truncated)
  engagements: [1.43, 0.32, 235.93, 214.94, 48.18, 25.24, 0.16, 5.06, 8.7, 32.67, 7.1, 8.94, 0.57, 1.3, 8.4, 2.93]
  engagements_c: [1.43, 0.32, 235.93, 214.94, 48.18, 25.24, 0.16, 5.06, 8.7, 32.67, 7.1, 8.94, 0.57, 1.3, 8.4, 2.93]
  id: 54434
  likes: 3000000
  avg_hearts_c: 12610.69
  image: https://p19-pu-useast8.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/2dd64f5509a46cfd24ea9cbb1da81ab0~c5...(truncated)
  comments: [0.0, 1.0, 174.0, 99.0, 77.0, 11.0, 0.0, 9.0, 4.0, 26.0, 17.0, 14.0, 1.0, 1.0, 14.0, 13.0]
  avg_hearts: 12610.69
  url: https://www.tiktok.com/@myageorgie/
  followers: 33600
  following: 243
  name: @myageorgie
  avg_engagement_c: 37.62
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/6750080a5c4a37706cdba90ba0105911.jpg?x-expires=1...(truncated)
  avg_comments_c: 28.81
  earnings_post: 28.31-44.49
  creator_gender: female
Score: 8.000
```

Node 4:
```
Node ID: trendingwithkennedi/
Text: ["Replying to @flexingingodspeace1 First #washday of the new y...", "Distressed Mom Jeans #DIY 💋 #ShowYourGlow #trendingwithkenne...", "i am literally the spoiled little sister 🥹🤍 i love it here !...", "girlies @Old Navy Official has your must have summer sets 😭🤍...", "my mom said i&rsquo;m going to meet her son-in-law in th...", "dinner party ready ✨🤍 #blackgirltiktok #grwm #outfit #ootd #...", "MY EYE WEAR PRADA @pradabeauty @SEPHORA #pradabeauty #gifte...", "what time do i need to be there bo...(truncated)
Metadata:
  comments_c: [7.0, 27.0, 5.0, 17.0, 8.0, 30.0, 6.0, 4.0, 4.0, 2.0, 6.0, 19.0, 95.0, 0.0, 4.0, 4.0]
  country: US
  avg_comments: 14.88
  hearts_c: [3430.0, 2220.0, 90.0, 96.0, 74.0, 115.0, 57.0, 152.0, 67.0, 25.0, 45.0, 1530.0, 8610.0, 26.0, 45.0,...(truncated)
  keys: ['skincare', 'fashion', 'beauty']
  bio: Estie K | Skincare + Fashion @trendingwithkennedi PROVERBS 16:3 future estie bestie ✨ ceo @myyummisk...(truncated)
  language: english
  creator_age: 20-24
  avg_engagement: 8.13
  platform: tiktok
  last_activity: 2024-05-22T17:22:22.815124000
  video_urls_tk: ['https://www.tiktok.com/@trendingwithkennedi/video/7185959042098007338/', 'https://www.tiktok.com/@trendingwithkennedi/video/7006500796019772678/', 'https://www.tiktok.com/@trendingwithkennedi/video/7361478749906275626/', 'https://www.tiktok.com/@trendingwithkennedi/video/7361115096824909102/', 'https://www.tiktok.com/@trendingwithkennedi/video/7357078472662994218/', 'https://www.tiktok.com/@trendingwithkennedi/video/7355320343705324846/', 'https://www.tiktok.com/@trendingwithkennedi/video/7354507082156100906/', 'https://www.tiktok.com/@trendingwithkennedi/video/7351854375339412782/', 'https://www.tiktok.com/@trendingwithkennedi/video/7346242818844708139/', 'https://www.tiktok.com/@trendingwithkennedi/video/7345240735865834798/', 'https://www.tiktok.com/@trendingwithkennedi/video/7341413621206994218/', 'https://www.tiktok.com/@trendingwithkennedi/video/7334532187414449438/', 'https://www.tiktok.com/@trendingwithkennedi/video/7308446519886155050/', 'https://www.tiktok.com/@trendingwithkennedi/video/7295600574022602026/', 'https://www.tiktok.com/@trendingwithkennedi/video/7292518061154864415/', 'https://www.tiktok.com/@trendingwithkennedi/video/7289883147062332702/']
  hearts: [3430.0, 2220.0, 90.0, 96.0, 74.0, 115.0, 57.0, 152.0, 67.0, 25.0, 45.0, 1530.0, 8610.0, 26.0, 45.0,...(truncated)
  engagements: [26.44, 17.28, 0.73, 0.87, 0.63, 1.12, 0.48, 1.2, 0.55, 0.21, 0.39, 11.92, 66.96, 0.2, 0.38, 0.72]
  engagements_c: [26.44, 17.28, 0.73, 0.87, 0.63, 1.12, 0.48, 1.2, 0.55, 0.21, 0.39, 11.92, 66.96, 0.2, 0.38, 0.72]
  id: 78104
  likes: 222200
  avg_hearts_c: 1042.00
  image: https://p16.tiktokcdn-us.com/tos-useast5-avt-0068-tx/7345610440157708334~c5_720x720.jpeg
  comments: [7.0, 27.0, 5.0, 17.0, 8.0, 30.0, 6.0, 4.0, 4.0, 2.0, 6.0, 19.0, 95.0, 0.0, 4.0, 4.0]
  avg_hearts: 1042.00
  url: https://www.tiktok.com/@trendingwithkennedi/
  followers: 13000
  following: 597
  name: @trendingwithkennedi
  avg_engagement_c: 8.13
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/790c72d6fdefbcb00d358d6319de7138.jpg?x-expires=1...(truncated)
  avg_comments_c: 14.88
  earnings_post: 10.5-16.5
  creator_gender: female
Score: 7.000
```

**Evaluation Results:**

- Faithfulness: 1.00 (Pass)
  - Explanation: YES
- Relevancy: 0.00
  - Explanation: NO
- Number of Source Nodes: 4
- Query Runtime: 19.84 seconds

### Query 5: recommend some cooking YouTubers

**Response:**

You might enjoy checking out the TikTok profiles of @mrs.culinary and @aima.nareswari, who both share content related to cooking and culinary tips. They are quite popular in their respective regions and offer a variety of recipes and cooking techniques that could be of interest to you.

**Source Nodes:**

Node 1:
```
Node ID: mrs.culinary/
Text: ["Sini saya kasih triknya bikin mini chiffon! Biar dagangan la...", "Buat utk mertua yukk. 3 Bahan Dessert tanpa oven! Rasa resto...", "Kayaknya makanan favorit semua orang. Awas ketagihan ya 🤭 #t...", "Saus andalan untuk segala lauk✨ #resep #ayamgorengmentega #u...", "Cuman dari sayuran bisa jadi menu Restoran✨ #sapotahu #capca...", "#disponsori Sat set sat set ga ribet! Saya bikin pudding can...", "Garingnya berjam jam pake trik ini✨ #lumpia #lumpiasayur #g...", "#disponsori Antri berjam jam t...(truncated)
Metadata:
  comments_c: [3180.0, 2920.0, 1440.0, 492.0, 119.0, 10.0, 93.0, 67.0, 100.0, 11.0, 24.0, 10.0, 8.0, 954.0, 13.0, ...(truncated)
  country: MY
  avg_comments: 479.65
  hearts_c: [1110000.0, 592980.0, 485950.0, 99690.0, 11810.0, 236.0, 10080.0, 3890.0, 14360.0, 908.0, 1450.0, 71...(truncated)
  keys: ['culinary', 'cooking', 'food']
  bio: Mrs. Culinary @mrs.culinary ⭐️ YouTube: 680K Subs ⭐️ DM IG for business   BELI DIMANA? 👇🏻 KLIK INI Y...(truncated)
  language: ['en', 'id', 'none']
  avg_engagement: 25.76
  platform: tiktok
  last_activity: 2024-05-07T17:23:36.771079000
  video_urls_tk: ['https://www.tiktok.com/@mrs.culinary/video/7300158446014336261/', 'https://www.tiktok.com/@mrs.culinary/video/7172856009759788315/', 'https://www.tiktok.com/@mrs.culinary/video/7161749525047053595/', 'https://www.tiktok.com/@mrs.culinary/video/7353584487457934597/', 'https://www.tiktok.com/@mrs.culinary/video/7353211310936444166/', 'https://www.tiktok.com/@mrs.culinary/video/7351403193017928965/', 'https://www.tiktok.com/@mrs.culinary/video/7350990247083265286/', 'https://www.tiktok.com/@mrs.culinary/video/7350239479422094597/', 'https://www.tiktok.com/@mrs.culinary/video/7346171523679407365/', 'https://www.tiktok.com/@mrs.culinary/video/7345789022297492741/', 'https://www.tiktok.com/@mrs.culinary/video/7332809922331053318/', 'https://www.tiktok.com/@mrs.culinary/video/7332074325677264134/', 'https://www.tiktok.com/@mrs.culinary/video/7330220201981562117/', 'https://www.tiktok.com/@mrs.culinary/video/7328364202744220933/', 'https://www.tiktok.com/@mrs.culinary/video/7327986607032749318/', 'https://www.tiktok.com/@mrs.culinary/video/7327249263342161158/', 'https://www.tiktok.com/@mrs.culinary/video/7324648922062851333/', 'https://www.tiktok.com/@mrs.culinary/video/7315006456623910150/', 'https://www.tiktok.com/@mrs.culinary/video/7314637880305995013/', 'https://www.tiktok.com/@mrs.culinary/video/7312408626046586118/', 'https://www.tiktok.com/@mrs.culinary/video/7308685640546209029/', 'https://www.tiktok.com/@mrs.culinary/video/7307570649008999686/', 'https://www.tiktok.com/@mrs.culinary/video/7306826427071089925/']
  hearts: [1110000.0, 592980.0, 485950.0, 99690.0, 11810.0, 236.0, 10080.0, 3890.0, 14360.0, 908.0, 1450.0, 71...(truncated)
  engagements: [241.94, 129.52, 105.93, 21.77, 2.59, 0.05, 2.21, 0.86, 3.14, 0.2, 0.32, 0.16, 0.3, 14.85, 0.97, 0.2...(truncated)
  engagements_c: [241.94, 129.52, 105.93, 21.77, 2.59, 0.05, 2.21, 0.86, 3.14, 0.2, 0.32, 0.16, 0.3, 14.85, 0.97, 0.2...(truncated)
  id: 53817
  likes: 4700000
  avg_hearts_c: 118065.13
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/f8db778c2d6ce0b9016e781b5aee46b5~c5_720x720.jpeg
  comments: [3180.0, 2920.0, 1440.0, 492.0, 119.0, 10.0, 93.0, 67.0, 100.0, 11.0, 24.0, 10.0, 8.0, 954.0, 13.0, ...(truncated)
  avg_hearts: 118065.13
  url: https://www.tiktok.com/@mrs.culinary/
  followers: 460100
  following: 281
  name: @mrs.culinary
  avg_engagement_c: 25.76
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/e72d59ff1c44ec6e28a78ecf96ac27c4.jpg?x-expires=1...(truncated)
  avg_comments_c: 479.65
  earnings_post: 349.77-549.64
Score: 10.000
```

Node 2:
```
Node ID: aima.nareswari/
Text: ["terimakasii untuk kesempatan yang berkesan✨️☺️ #kknugm...", "dari sekian lipatan mana yang paling sering di liat? ☺️#boga...", "di balik Tugas Mahasiswa Pendidikan Teknik Boga semester 1. ...", "Tebak aku magang di mana wkwk #bogauny #boga #culinary #mag...", "Jadi boleh atau engga? #bogauny #boga #culinary #magang #jo...", "Maaf yaa jadi jarang upload 🥹 #bogauny #boga #culinary #maga...", "Masak masakk lagiii hihihi 🥰🫶🏻 #bogauny #boga #culinary ...", "Akutunggu sampai kamu nyobain juga ya ✨😚 ...(truncated)
Metadata:
  comments_c: [1510.0, 5200.0, 4260.0, 25.0, 19.0, 31.0, 35.0, 11.0, 12.0, 6.0, 14.0, 16.0, 14.0, 309.0, 36.0, 79....(truncated)
  country: ID
  avg_comments: 530.74
  hearts_c: [296830.0, 1100000.0, 913820.0, 2510.0, 3660.0, 1260.0, 6240.0, 846.0, 882.0, 678.0, 1070.0, 1150.0,...(truncated)
  keys: ['culinary', 'cooking', 'food']
  bio: aima|boga🍛 @aima.nareswari Perjalanan Mahasiswa Pendidikan Tata Boga  do what u love and try to play...(truncated)
  language: Indonesian
  avg_engagement: 65.08
  platform: tiktok
  last_activity: 2024-04-24T21:02:44.884014000
  video_urls_tk: ['https://www.tiktok.com/@aima.nareswari/video/7127497467964312859/', 'https://www.tiktok.com/@aima.nareswari/video/7116439410463264026/', 'https://www.tiktok.com/@aima.nareswari/video/7116055544288382235/', 'https://www.tiktok.com/@aima.nareswari/video/7359412610527284485/', 'https://www.tiktok.com/@aima.nareswari/video/7358650998690270470/', 'https://www.tiktok.com/@aima.nareswari/video/7358401243989036294/', 'https://www.tiktok.com/@aima.nareswari/video/7351311556220767493/', 'https://www.tiktok.com/@aima.nareswari/video/7349474273678904581/', 'https://www.tiktok.com/@aima.nareswari/video/7348627266215185669/', 'https://www.tiktok.com/@aima.nareswari/video/7345788693875035397/', 'https://www.tiktok.com/@aima.nareswari/video/7341599982115474693/', 'https://www.tiktok.com/@aima.nareswari/video/7340535797285719301/', 'https://www.tiktok.com/@aima.nareswari/video/7340110338186104070/', 'https://www.tiktok.com/@aima.nareswari/video/7338426491954334982/', 'https://www.tiktok.com/@aima.nareswari/video/7336035002834078982/', 'https://www.tiktok.com/@aima.nareswari/video/7333416616643890437/', 'https://www.tiktok.com/@aima.nareswari/video/7331956375305669893/', 'https://www.tiktok.com/@aima.nareswari/video/7331426211085700357/', 'https://www.tiktok.com/@aima.nareswari/video/7328236468676087046/', 'https://www.tiktok.com/@aima.nareswari/video/7325355187927895302/', 'https://www.tiktok.com/@aima.nareswari/video/7323809889229327622/', 'https://www.tiktok.com/@aima.nareswari/video/7323146740796853510/', 'https://www.tiktok.com/@aima.nareswari/video/7321226913630964997/']
  hearts: [296830.0, 1100000.0, 913820.0, 2510.0, 3660.0, 1260.0, 6240.0, 846.0, 882.0, 678.0, 1070.0, 1150.0,...(truncated)
  engagements: [177.58, 657.86, 546.48, 1.51, 2.19, 0.77, 3.74, 0.51, 0.53, 0.41, 0.65, 0.69, 1.1, 16.55, 1.29, 15....(truncated)
  engagements_c: [177.58, 657.86, 546.48, 1.51, 2.19, 0.77, 3.74, 0.51, 0.53, 0.41, 0.65, 0.69, 1.1, 16.55, 1.29, 15....(truncated)
  id: 4376
  likes: 8000000
  avg_hearts_c: 108804.61
  image: https://p16-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/531962c60236fe1608ff7bf3f6d623be~c5_72...(truncated)
  comments: [1510.0, 5200.0, 4260.0, 25.0, 19.0, 31.0, 35.0, 11.0, 12.0, 6.0, 14.0, 16.0, 14.0, 309.0, 36.0, 79....(truncated)
  avg_hearts: 108804.61
  url: https://www.tiktok.com/@aima.nareswari/
  followers: 168000
  following: 236
  name: @aima.nareswari
  avg_engagement_c: 65.08
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/7cbe71a2db9813476f7d7d5f19e25753.jpg?x-expires=1...(truncated)
  avg_comments_c: 530.74
  earnings_post: 125.65-197.44
Score: 9.000
```

Node 3:
```
Node ID: kaitlinharasta/
Text: ["This is how I get the groceries for my job, as chef/stew on ...", "All to ourselves #fyp #byronbay #foryoupage", "Working in my home town 🇦🇺 #privatechef #food #sydney #foryo...", "apparently peeling pomegranates for your loved one is a thin...", "the best sunset ive maybe ever seen #fiji #yachtchef #privat...", "my favorite cuisine to make 🇯🇵 #yachtchef #fiji #chef #sushi...", "the best way to start the day 😭❤️ #yachtchef #chef #orcas #f...", "Kokoda is never a bad idea 🤤 #fiji #yachtchef #fi...(truncated)
Metadata:
  comments_c: [30.0, 287.0, 6.0, 8.0, 5.0, 12.0, 20.0, 108.0, 37.0, 16.0, 2.0, 8.0, 64.0, 11.0, 6.0, 18.0, 37.0, 1...(truncated)
  country: ES
  avg_comments: 32.55
  hearts_c: [30400.0, 27600.0, 277.0, 718.0, 1730.0, 2090.0, 3440.0, 20680.0, 49430.0, 19310.0, 230.0, 933.0, 50...(truncated)
  keys: ['chef', 'cooking', 'culinary']
  bio: kaitlin.harasta @kaitlinharasta I cook 👩🏽‍🍳  Insta: kaitlinharasta & thebikinicook
  language: ['en', 'none', 'fr']
  avg_engagement: 46.27
  platform: tiktok
  last_activity: 2024-05-19T16:58:38.090274000
  video_urls_tk: ['https://www.tiktok.com/@kaitlinharasta/video/6809593778882514182/', 'https://www.tiktok.com/@kaitlinharasta/video/6911686725660101890/', 'https://www.tiktok.com/@kaitlinharasta/video/7366501799416663313/', 'https://www.tiktok.com/@kaitlinharasta/video/7347270681446403330/', 'https://www.tiktok.com/@kaitlinharasta/video/7346175729685630209/', 'https://www.tiktok.com/@kaitlinharasta/video/7340628354846002433/', 'https://www.tiktok.com/@kaitlinharasta/video/7339698701654445313/', 'https://www.tiktok.com/@kaitlinharasta/video/7338375208677657858/', 'https://www.tiktok.com/@kaitlinharasta/video/7337901855906778370/', 'https://www.tiktok.com/@kaitlinharasta/video/7336190710204452097/', 'https://www.tiktok.com/@kaitlinharasta/video/7335286899751259394/', 'https://www.tiktok.com/@kaitlinharasta/video/7334681721448844546/', 'https://www.tiktok.com/@kaitlinharasta/video/7331213566382492929/', 'https://www.tiktok.com/@kaitlinharasta/video/7330905400964844801/', 'https://www.tiktok.com/@kaitlinharasta/video/7330054433524550914/', 'https://www.tiktok.com/@kaitlinharasta/video/7328928190292937985/', 'https://www.tiktok.com/@kaitlinharasta/video/7327784955310820609/', 'https://www.tiktok.com/@kaitlinharasta/video/7326718025573403905/', 'https://www.tiktok.com/@kaitlinharasta/video/7326473655590997249/', 'https://www.tiktok.com/@kaitlinharasta/video/7241424886864874753/', 'https://www.tiktok.com/@kaitlinharasta/video/7220042671736245505/', 'https://www.tiktok.com/@kaitlinharasta/video/7213982473401732354/']
  hearts: [30400.0, 27600.0, 277.0, 718.0, 1730.0, 2090.0, 3440.0, 20680.0, 49430.0, 19310.0, 230.0, 933.0, 50...(truncated)
  engagements: [142.86, 130.92, 1.33, 3.41, 8.15, 9.87, 16.24, 97.6, 232.24, 90.73, 1.09, 4.42, 238.19, 5.17, 2.7, ...(truncated)
  engagements_c: [142.86, 130.92, 1.33, 3.41, 8.15, 9.87, 16.24, 97.6, 232.24, 90.73, 1.09, 4.42, 238.19, 5.17, 2.7, ...(truncated)
  id: 40061
  likes: 262600
  avg_hearts_c: 9822.14
  image: https://p16.tiktokcdn.com/tos-maliva-avt-0068/7331423806051450885~c5_720x720.jpeg
  comments: [30.0, 287.0, 6.0, 8.0, 5.0, 12.0, 20.0, 108.0, 37.0, 16.0, 2.0, 8.0, 64.0, 11.0, 6.0, 18.0, 37.0, 1...(truncated)
  avg_hearts: 9822.14
  url: https://www.tiktok.com/@kaitlinharasta/
  followers: 21300
  following: 55
  name: @kaitlinharasta
  avg_engagement_c: 46.27
  video_thumbnails: ["https://p16-amd-sg.axod.net/obj/tos-maliva-p-0068/6a15346fdaf8c8fe7bb9ed8a03da7414.jpg?x-expires=1...(truncated)
  avg_comments_c: 32.55
  earnings_post: 15.99-25.13
Score: 8.000
```

**Evaluation Results:**

- Faithfulness: 0.00 (Fail)
  - Explanation: NO
- Relevancy: 0.00
  - Explanation: NO
- Number of Source Nodes: 3
- Query Runtime: 16.89 seconds


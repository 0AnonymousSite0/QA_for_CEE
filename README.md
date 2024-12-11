# Building the knowledge graph of construction engineering economics to augment question-answering performance of general-purpose LLMs: A case of China

## !!! As the paper is under review, all materials in this repository currently are not allowed to be re-used by anyone until this announcement is deleted.

# 0. Videos of running original LLMs, CEE knowledge-incorporated LLMs, and CEE-QA prototype

![GIF for running video of original LLMs](https://github.com/user-attachments/assets/310641bb-7534-4ce8-b24d-8d019d9e2dcb)

↑↑↑Multiple original LLMs simultaneously answering the CEE-related questions

![GIF for running video of CEE knowledge-incorporated LLMs](https://github.com/user-attachments/assets/336a4854-279c-4a3a-8f79-6d3699c737ad)

↑↑↑Multiple CEE knowledge-incorporated LLMs simultaneously answering the CEE-related questions

![GIF for running video of CEE-QA prototype](https://github.com/user-attachments/assets/afd6f4c4-45fc-4cc4-ba82-7f2d55ac0d2b)

↑↑↑CEE-QA prototype answering the CEE-related question

# 1. General introduction of this repository

1.1 This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by University of XXX in UK and XXX University in China.

1.2 We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including langchain, llamaindex, openai, chatglm, numpy, and so on. Our work stands on the shoulders of these giants.

1.3 As for anything regarding the copyright, please refer to the MIT License or contact the authors.

# 2. Summary of supplemental materials in this repository

The table below shows all supplemental materials. All sheets in Tables S1, S2, and S3 are arranged in the order shown in this table.

![Inventory of supplemental materials](https://github.com/user-attachments/assets/caecc6e5-9e3b-40eb-a7da-baefa8f7e41b)

All supplemental materials are provided in the GitHub repository (https://github.com/0AnonymousSite0/QA_for_CEE). Besides the GitHub repository, the CEE-QA test question set is shared in the Hugging Face repository (https://huggingface.co/datasets/AnonymousSite/QA_test_question_set_for_CEE).

# 3. LLM Leaderboard for CEE-QA

The test results of different LLMs on the CEE-QA test question set are shown below. Welcome global scholars to test their LLM works on CEE-QA, please see the following specification of reusing the QA question set.

| General-purpose large language models |	Contributors |	Average correctness ratio |	KSD1 |	KSD2 |	KSD3 |	KSD4 |	KSD5 |	KSD6	| KSD7 |	KSD8 |	KSD9 |	KSD10 |	KSD11 |	KSD12 |	KSD13 |	KSD14 |	KSD15  | KSD16	| KSD17 |	KSD18 |	Ranking |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Knowledge-incorporated ERNIE-Bot-turbo4.0 |	Baidu & The authors |	0.7778 |	0.7419 |	0.7869 |	0.6883 |	0.6834 |	0.7961 |	0.8539 |	0.7746 |	0.8889 |	0.8070 | 0.8618 | 0.8706 | 0.9155 |	0.7188 | 0.7813 |	0.7770 |	0.7902 |	0.7205 |	0.8368 | 1 |
| Original ERNIE-Bot-turbo4.0 |	Baidu |	0.7389 |	0.7097 |	0.7732 |	0.6753 |	0.6154 |	0.7913 |	0.8371 |	0.7664 |	0.7460 |	0.7719 |	0.8487 |	0.8000 | 0.7817 | 0.6953 |	0.7344 |	0.7338 |	0.7816 |	0.6568 |	0.7737 | 2 |
| Knowledge-incorporated GPT-4 | OpenAI & The authors |	0.6389 |	0.5403 | 0.6475 | 0.6753 |	0.5858 | 0.6214 | 0.7978 | 0.6926 | 0.6905 | 0.5789 | 0.7862 | 0.8294 | 0.8662 | 0.5215 | 0.6172 |	0.5935 | 0.5862 | 0.6182 | 0.6632 | 3 |
| Original GPT-4 |	OpenAI |	0.5452 |	0.5215 |	0.6066 |	0.5974 |	0.4675 |	0.5388 |	0.7022 |	0.6270 |	0.6349 |	0.5702 |	0.7599 |	0.7353 |	0.6338 |	0.4160 |	0.4883 |	0.4460 |	0.4023 |	0.5000 |	0.6053 |	4 |
| Knowledge-incorporated Baichuan2-13b	| Baichuan AI & The authors |	0.4772 |	0.4328 |	0.4754 |	0.5065 |	0.4379 |	0.4272 |	0.6180 |	0.4959 |	0.5556 |	0.3509 |	0.6546 |	0.4235 | 0.5211 |	0.4199 |	0.4961 |	0.4460 |	0.4655 |	0.4409 |	0.5474 |	5 |
| Knowledge-incorporated GPT-3.5-turbo |	OpenAI & The authors |	0.4650 |	0.4651 |	0.4617 |	0.4610 |	0.3935 |	0.5097 |	0.5674 |	0.5082 |	0.5159 |	0.3509 |	0.6480 |	0.5471 | 0.5986 |	0.3770 |	0.4688 |	0.4460 |	0.3822 |	0.3909 |	0.5526 |	6 |
| Knowledge-incorporated Baichuan2-7b |	Baichuan AI & The authors |	0.4618 |	0.4328 |	0.4754 |	0.5065 |	0.4379 |	0.4272 |	0.6180 |	0.4959 |	0.5556 |	0.3509 |	0.6546 |	0.4235 | 0.5211 |	0.4199 |	0.4961 |	0.4460 |	0.4655 |	0.4409 |	0.5474 |	7 |
| Knowledge-incorporated ChatGLM3-6b |	Tsinghua & The authors |	0.4603 |	0.4328 |	0.4126 |	0.4610 |	0.4083 |	0.4466 |	0.5955 |	0.5287 |	0.4444 |	0.4123 |	0.5954 |	0.4588 |	0.5563 |	0.4219 |	0.4727 |	0.4964 |	0.4454 |	0.4023 |	0.4474 |	8 |
| Knowledge-incorporated ERNIE-Bot-turbo |	Baidu & The authors	| 0.4470 |	0.4032 |	0.4918 |	0.5649 |	0.3757 |	0.4369 |	0.5955 |	0.4836 |	0.4444 |	0.5088 |	0.5954 |	0.4176 |	0.5845 |	0.3906 |	0.4219 |	0.3957 |	0.3764 |	0.3591 |	0.5474 |	9 |
| Knowledge-incorporated Qianfan-Chinese-Llama-2-7B |	Baidu & The authors |	0.4453 |	0.4489 |	0.3962 |	0.4545 |	0.4438 |	0.4466 |	0.5730 |	0.4754 |	0.5079 |	0.3246 |	0.5362 |	0.4588 |	0.5704 |	0.3613 |	0.5000 |	0.4496 |	0.4080 |	0.4023 |	0.4632 |	10 |
| Original Baichuan2-13b |	Baichuan AI | 0.4312 |	0.4032 |	0.4235 |	0.4545 |	0.4083 |	0.3883 |	0.5899 |	0.4836 |	0.4921 |	0.3509 |	0.5921 |	0.4118 |	0.4366 |	0.4023 |	0.3945 |	0.3273 |	0.4138 |	0.4091 |	0.4789 |	11 |
| Original Baichuan2-7b	| Baichuan AI	| 0.4057 |	0.3737 |	0.4426 |	0.3636 |	0.3639 |	0.4126 |	0.5281 |	0.4631 |	0.4603 |	0.2632 |	0.5230 |	0.3294 |	0.4437 |	0.3789 |	0.4219 |	0.3849 |	0.3879 |	0.3636 |	0.4211 |	12 |
| Original GPT-3.5-turbo |	OpenAI	| 0.4016 |	0.3844 |	0.4071 |	0.3896 |	0.3254 |	0.4272 |	0.5169 |	0.4549 |	0.4444 |	0.3246 |	0.6020 |	0.4765 |	0.4225 |	0.3594 |	0.4023 |	0.3345 |	0.3247 |	0.3568 |	0.4368 |	13 |
| Original ERNIE-Bot-turbo |	Baidu	| 0.3873 |	0.3871 |	0.3880 |	0.5519 |	0.3432 |	0.3883 |	0.5112 |	0.4344 |	0.4127 |	0.4474 |	0.5132 |	0.3000 |	0.4648 |	0.3223 |	0.4141 |	0.3094 |	0.3218 |	0.3409 |	0.4000 |	14 |
| Original ChatGLM3-6b	| Tsinghua	| 0.3837 |	0.3656 |	0.3825 |	0.3377 |	0.2574 |	0.3932 |	0.5618 |	0.4467 |	0.3571 |	0.3070 |	0.5329 |	0.3588 |	0.4296 |	0.3730 |	0.3516	| 0.3993 |	0.3764 |	0.3477 |	0.3842 |	15 |
| Original Qianfan-Chinese-Llama-2-7B	| Baidu	| 0.3740 |	0.4194 |	0.3251 |	0.4481 |	0.3402 |	0.4417 |	0.4831 |	0.4713 |	0.3810 |	0.2807 |	0.4967 |	0.3000 |	0.3310 |	0.3301 |	0.4219 |	0.3597 |	0.3420 |	0.2818 |	0.3789 |	16 |
| Knowledge-incorporated Llama-2-13b	| Meta AI & The authors	| 0.3189 |	0.3226 |	0.2732 |	0.3377 |	0.3521 |	0.2718 |	0.3202 |	0.2705 |	0.3254 |	0.3509 |	0.3618 |	0.3765 |	0.3521 |	0.2734 |	0.3555 |	0.3345 |	0.2845 |	0.3023 |	0.4211 |	17 |
| Original Llama-2-13b	| Meta AI |	0.2596 |	0.2903 |	0.2022 |	0.3052 |	0.2574 |	0.2330 |	0.2753 |	0.2582 |	0.2778 |	0.2807 |	0.2796 |	0.2471 |	0.3310 |	0.2422 |	0.2461 | 0.2482 |	0.2155 |	0.2773 |	0.3158 |	18 |

# 4. Reuse of the CEE-KG with three optional versions

![Three optional versions of CEE-KG](https://github.com/user-attachments/assets/4afb80a9-3d02-4ecd-a360-f0ed6bd4ad8a)

↑↑↑Three optional versions of CEE-KG

The CEE-KG is available through this link (https://drive.google.com/drive/folders/1TnIMULnN3V1R3GsU-aFy64AdCx6lEVaK?usp=drive_link).


# 5. Reuse of the CEE-QA question set

The CEE-QA test question set containing 2,921 questions is manually annotated with four features, including the question source, single-answer question or multiple-answer question, and calculation question or non-calculation question.

![CEE-QA test question set in the Hugging Face repository](https://github.com/user-attachments/assets/c99832e5-16c4-430e-a596-32700d94bc51)

↑↑↑The CEE-QA test question set in the Hugging Face repository

More information about the qustion set can be found through these links (https://huggingface.co/datasets/AnonymousSite/QA_test_question_set_for_CEE)

# 6. Reuse of the codes for running original LLMs, CEE knowledge-incorporated LLMs and CEE-QA prototype

## 6.1 Environment set

All codes are developed on Python 3.10, and the IDE adopted is PyCharm (Professional version). The codes also support GPU computing for higher speed; the Navida CUDA we adopted is V10.0.130. The GIS platform is Arcgis Pro 2.3, and its license is necessary. 

aiohttp==3.9.3

aiolimiter==1.1.0

appdirs==1.4.4

asgiref==3.7.2

atomicwrites==1.4.0

backoff==2.2.1

backports.weakref==1.0.post1

bce-python-sdk==0.9.4

bcrypt==4.1.2

brotlipy==0.7.0

build==1.0.3

......

Please refer to the supplementary materials for the complete requirement file.

Before submitting these codes to Github, all of them have been tested to be well-performed (as shown in the images). Even so, we are not able to guarantee their operation in other computing environments due to the differences in the Python version, computer operating system, and adopted hardware.

## 6.2 Codes for running the LLMs

Closed-source LLMs are API-only, and open-source LLMs are deployed directly on the AutoDL Cloud server.

![Codes for running CEE original LLMs](https://github.com/user-attachments/assets/fe16aa00-a88c-4078-b216-59c1ed142874)

↑↑↑Codes for running original LLMs

![Codes for running CEE knowledge-incorporated LLMs](https://github.com/user-attachments/assets/e8172a3b-39be-4265-b6b5-77fae383bdca)

↑↑↑Codes for running CEE knowledge-incorporated LLMs

![Codes for deploying and running the CEE-QA prototype](https://github.com/user-attachments/assets/f0dc7543-c729-44f5-af82-eab18aca8462)

↑↑↑Codes for deploying and running CEE-QA prototype













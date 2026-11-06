---
title: "Methods Monday | 14 September 2026"
date: 2026-09-14
type: other
url: https://varna.substack.com/p/methods-monday-14-september-2026
subtitle: "The strongest methods work this week asks a deceptively simple question: how much of a survey result is created by the machinery of measurement itself? "
source: varna.substack.com, fetched by scripts/sync_substack.py
---

# Methods Monday | 14 September 2026

*2026-09-14. Published at [https://varna.substack.com/p/methods-monday-14-september-2026](https://varna.substack.com/p/methods-monday-14-september-2026). This file is a generated copy; the Substack post is the original.*

[![Editorial illustration for Methods Monday showing the same survey question in English, Hindi, Bangla, Urdu and Tamil, alongside a South Asia map, magnifying glass, charts, translation notes and measuring tools.](https://substackcdn.com/image/fetch/$s_!FdXh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68881d08-5bff-4477-b354-a68402f2df42_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!FdXh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68881d08-5bff-4477-b354-a68402f2df42_1536x1024.png)
*Methods Monday - 14th September 2026*

*Translation choices move means. AI coding performs differently across languages. Fieldwork stopping rules trade cost against uncertainty. Synthetic respondents reproduce some patterns while distorting others. For researchers working across multilingual and uneven survey environments in South Asia, these are practical problems.*

## 1. translation can change the statistics, even when every version looks defensible

Chia-Jung Tsai, Clemens Lechner, Dorothée Behr, Ulrike Efu Nkong and Anke Radinger provide unusually direct evidence on questionnaire translation. They asked 16 professional translators and 16 social scientists to translate an English questionnaire into German, using both translation from scratch and human post-editing of machine translation. The resulting 32 questionnaire versions were fielded separately. The analysis ultimately covered 8,377 completed interviews, with roughly 250 responses for each experimental translation.

The differences were not trivial. Item means varied across translations, sometimes substantially. Post-editing machine translation reduced variation between versions and generally brought results closer to the official benchmark. It introduced a different risk: a subtle error in the machine version could survive human review and produce systematic bias. Social scientists translating from scratch were slightly more likely than professional translators to generate statistical outliers.

For South Asian survey research, the application is immediate. Translation is still routinely treated as an operational task after questionnaire design. This paper shows that wording decisions can change the distribution of the variable itself. Back-translation does not solve that problem. The authors make a stronger case for collaborative procedures such as translation, review, adjudication, pretesting and documentation.

Tsai, Chia-Jung, Clemens Lechner, Dorothée Behr, Ulrike Efu Nkong and Anke Radinger. 2026. “The Influence of Translator Backgrounds and Machine Translation on Statistical Properties of Surveys: Evidence from a Survey Experiment.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smag029. Published 9 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article/doi/10.1093/jssam/smag029/8789599?utm_source=chatgpt.com)

[Subscribe now](https://varna.substack.com/subscribe?)

**Worth reading: first on my list this week.**

## 2. LLM coding works reasonably well across several languages, then drops in a lower-resource one

Mao Li, Stephanie Morales, Kaidar Nurumov and Sunghee Lee test whether large language models can code open-ended responses to a web probe attached to the familiar self-rated health question. Their data span five countries and four languages. Five open-source LLMs were compared with human coding and conventional machine-learning models.

The best model reached a micro-F1 score of 0.76 when classifying attributes mentioned in respondents’ answers and 0.77 when classifying whether those attributes were expressed positively, negatively or neutrally. Performance remained fairly stable for English, Spanish and German, then fell for Korean. The authors link the difference to Korean’s lower representation in model training data.

The South Asian implication is an inference rather than something this paper establishes. Performance on English gives us little basis for assuming similar accuracy in Bangla, Sinhala, Tamil, Nepali, Urdu or lower-resource Indian languages. Any LLM-assisted coding workflow used in multilingual research should therefore validate performance separately by language. A pooled accuracy figure can conceal where the model is failing.

Li, Mao, Stephanie Morales, Kaidar Nurumov and Sunghee Lee. 2026. “Using Large Language Models to Autocode Probing Responses to the Self-Rated Health Question: Strengths and Weaknesses in a Multilingual Survey Context.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smaf059. Published 9 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smaf059/8789739?utm_source=chatgpt.com)

**Worth reading: yes, especially for multilingual mixed-methods work.**

## 3. when should field teams stop calling?

Xinyu Zhang, James Wagner and Michael R. Elliott take on an ordinary fieldwork decision with large budget consequences. Continued attempts may bring harder-to-reach respondents into the sample, while each additional call costs money and may contribute little to the estimates a survey was designed to produce.

Their proposed risk-conscious stopping rule explicitly incorporates uncertainty in predicted survey costs and errors. Using Health and Retirement Study data and Monte Carlo simulations, they examine both which unresolved cases to stop pursuing and when that decision should be made. In several scenarios, implementing the rule after eight to ten call attempts produced the lowest number of attempts per completed interview while maintaining the same level of data quality for the statistics under study.

The method suits repeated surveys with good historical paradata and a small set of priority estimates. Transfer to one-off development surveys is less straightforward. A stopping rule based on poor predictions of response propensity or outcomes can simply formalise the wrong decision.

Zhang, Xinyu, James Wagner and Michael R. Elliott. 2026. “Optimizing Survey Errors and Survey Costs: A Risk-Conscious Stopping Rule and Timing Analysis.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smaf065. Published 9 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smaf065/8789740?utm_source=chatgpt.com)

**Worth reading: particularly useful for CATI panels, longitudinal surveys and repeated monitoring rounds.**

[Subscribe now](https://varna.substack.com/subscribe?)

## 4. a refusal to receive survey questions by text may not be a permanent refusal

Jim Vine and colleagues use two waves of the Understanding Society Innovation Panel to examine consent for receiving occasional survey questions by SMS. Overall, 69 per cent of respondents with mobile phones consented when asked. Among people who had refused when asked previously, 55 per cent consented when asked again at a later wave.

Mode mattered. In one wave, 65 per cent of web respondents consented compared with 78 per cent interviewed face to face. Because respondents could move between modes, the authors also exploit randomized initial mode allocation. The estimated mode effect is less precise, but the pattern still suggests that consent itself can be sensitive to how the request is made. Moving the consent question from early to late in the questionnaire changed consent by only 2.4 percentage points and the difference was statistically uncertain.

This is useful for development research adopting SMS follow-ups, rapid phone modules and panel recontact. Consent should not automatically be treated as a fixed respondent characteristic. Timing, mode and previous contact history may shape it.

Vine, Jim, et al. 2026. “Getting Consent to Survey in New Ways: Evidence from Experiments about Questions by Text Message in the Understanding Society Innovation Panel.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smag015. Published 9 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article/doi/10.1093/jssam/smag015/8789737?utm_source=chatgpt.com)

**Worth reading: useful if your study plans repeated respondent contact across modes.**

## 5. synthetic respondents need their own error framework

Indira Sen, Georg Ahnert, Leah von der Heyde, Jana Lasser, Bernd Weiß and Markus Strohmaier have proposed a Total Simulated Survey Error framework for studies in which LLMs are asked to act as survey respondents.

The paper starts from a problem that is becoming harder to ignore. A synthetic sample can reproduce aggregate human response patterns while getting subgroup distributions, associations between variables or particular populations wrong. Their framework separates representation and measurement problems and adds errors specific to simulation design, including the construction of respondent personas and choices about prompts and model settings. The authors illustrate the framework through simulated responses concerning the 2024 US presidential election.

The framework is more useful than another demonstration that a model can imitate an average respondent. For development research, synthetic respondents remain a poor substitute for empirical observation where the purpose is population inference. The framework gives researchers a better vocabulary for showing why.

Sen, Indira, Georg Ahnert, Leah von der Heyde, Jana Lasser, Bernd Weiß and Markus Strohmaier. 2026. “Total Simulated Survey Error: Designing and Diagnosing Survey Responses from Large Language Models.” arXiv:2609.10280. Posted 9 September 2026.

[Read the preprint](https://arxiv.org/abs/2609.10280?utm_source=chatgpt.com)

**Worth reading: yes, particularly before using synthetic data as anything beyond exploratory material.**

## 6. administrative data can show who a survey is systematically missing

Michael Jackson and colleagues use voter records, consumer databases and small-area contextual information to examine differential nonresponse in a US address-based survey. They could match 86 per cent of sampled addresses to voter or consumer databases. A model of partisan leaning agreed with respondents’ reported political leaning in 65 per cent of matched cases. Adding predicted partisanship to demographic weighting improved recalled-vote estimates, while validated turnout information improved them further.

The electoral application is specialised. The design idea travels well. Most surveys contain detailed data on respondents and almost nothing on nonrespondents. Administrative or frame data available for everyone sampled can turn nonresponse from an invisible problem into something that can at least be studied.

For South Asian research, feasibility depends on the source. Programme registers, school records, health-system lists and geographic covariates may sometimes provide the relevant frame information. Privacy, identifier quality and incomplete registers remain real constraints.

Jackson, Michael, et al. 2026. “Who are We Missing? Using Administrative and Contextual Data to Measure and Correct Partisan Nonresponse in Opinion Surveys.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smag017. Published 9 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag017/8789736?utm_source=chatgpt.com)

**Worth reading: yes. The substantive case is US-specific; the nonresponse design is useful much more widely.**

[Subscribe now](https://varna.substack.com/subscribe?)

## 7. web recruitment can accumulate educational bias at several different stages

Christine Distler, Mustafa Coban and Mark Trappmann examine recruitment into Germany’s IAB-OPAL online panel using administrative employment histories available for respondents and nonrespondents. Educational bias did not arise at one moment. It increased as people moved through successive stages of recruitment and registration.

People with lower secondary education made up 23.2 per cent of the gross sample and 11.1 per cent of those starting the first-wave interview, a 12.1 percentage-point difference. The study also finds interactions between education and characteristics such as age, nationality and gender. That matters because simply calibrating weights to the population distribution of education assumes away these interactions unless they are explicitly modelled.

The paper was published on 2 September, so it just falls outside this week’s release window. I am including it because it complements the new nonresponse work above and has direct relevance to the growth of push-to-web and digital-first surveys in development research.

Distler, Christine, Mustafa Coban and Mark Trappmann. 2026. “Nonresponse in Web Surveys: A Deeper Look into Education Bias.” *Journal of Survey Statistics and Methodology*. DOI: 10.1093/jssam/smag031. Published 2 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article/doi/10.1093/jssam/smag031/8780203?utm_source=chatgpt.com)

**Worth reading: high priority for anyone moving probability samples online.**

## south asia methods watch: Sri Lanka launches a three-route citizen feedback survey

Sri Lanka launched SL-PULSE on 10 September, a national system for measuring citizens’ experiences of public services across all 25 districts and 341 Divisional Secretariats. The programme expects to collect between 13,000 and 15,000 responses through three routes: open public participation, community-based field surveys and independent university-led household surveys.

That design makes SL-PULSE interesting as a measurement exercise. The three routes imply very different selection mechanisms. Open digital participation offers speed and scale, while the resulting respondents cannot simply be assumed to represent the population. The household component could provide a reference point, depending on how its sample is drawn and how estimates across streams are combined.

The public material currently describes seven governance areas, including service delivery, administrative procedures, accountability, corruption, environmental governance and digital governance. It does not yet provide enough technical detail to judge weighting, questionnaire validation or integration of the three samples.

[Read the UNDP announcement](https://www.undp.org/srilanka/press-releases/sl-pulse-jnridm-janaraitama-first-its-kind-digital-survey-tool-strengthen-citizen-centred-public-service-reforms?utm_source=chatgpt.com)

**Worth watching: yes. I would reserve judgement on the resulting indicators until the technical documentation appears.**

## also worth watching: Pakistan combines demographic and health survey systems

Pakistan’s 2026–27 Demographic and Health Survey is being developed within the Pakistan Bureau of Statistics after a government decision to integrate demographic, health, fertility and mortality modules into the existing Pakistan Demographic Survey architecture. PBS says it has reviewed both questionnaire content and survey methodology through technical consultations and plans national and provincial estimates covering population, fertility, maternal and child health, nutrition, mortality, family planning, gender and early childhood development.

The institutional change is methodologically interesting because consolidation can reduce duplication and respondent burden while creating comparability problems. Changes in sampling, question wording, field protocols or survey ownership can produce breaks in time series that later look like substantive change.

The next things to look for are the final sampling design, questionnaires and documentation showing how the 2026–27 series maps onto the 2017–18 PDHS.

[Pakistan Bureau of Statistics PDHS page](https://www.pbs.gov.pk/elementor-28549/?utm_source=chatgpt.com)

**Worth watching rather than reading: the technical documents will matter more than the announcement.**

## what I would read first

Start with Tsai et al. on translation. For multilingual work in South Asia, it addresses a source of measurement error that is routine, consequential and poorly documented. Li et al. comes next if you work with open text or automated coding. Zhang et al. is the most useful piece for fieldwork management. Sen et al. is the one I would keep nearby when somebody proposes replacing respondents with synthetic ones.

The thread running through this week is fairly plain. Survey error often enters before estimation begins. A different translation, recruitment route, coding system or decision about when to stop fieldwork can alter the dataset that later appears in a regression table. Statistical sophistication downstream does not recover information that the measurement process distorted upstream.

[Share](https://varna.substack.com/p/methods-monday-14-september-2026?utm_source=substack&utm_medium=email&utm_content=share&action=share)

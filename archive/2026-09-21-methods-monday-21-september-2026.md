---
title: "Methods Monday | 21 September 2026"
date: 2026-09-21
type: other
url: https://varna.substack.com/p/methods-monday-21-september-2026
subtitle: "Voice responses, SMS contact, rooftop sampling and small-area estimation, and where each method shifts survey error."
source: varna.substack.com, fetched by scripts/sync_substack.py
---

# Methods Monday | 21 September 2026

*2026-09-21. Published at [https://varna.substack.com/p/methods-monday-21-september-2026](https://varna.substack.com/p/methods-monday-21-september-2026). This file is a generated copy; the Substack post is the original.*

[![Editorial desk illustration for Methods Monday showing a household questionnaire, SMS survey invitation, rooftop sampling map, district-level estimates, field notes and measuring tools.](https://substackcdn.com/image/fetch/$s_!JFA5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7344e2d-ef6f-42d0-98d9-ffe837f526d4_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!JFA5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7344e2d-ef6f-42d0-98d9-ffe837f526d4_1536x1024.png)
*Methods Monday - 21 September 2026*

This is a short issue. The week’s useful methods work concerns voice responses, SMS contact and small-area estimation. I have also gone back for two recent papers we missed, including an India study on replacing household listing with satellite-derived rooftop data.

## 1. speaking produces richer open-ended answers. It also produces far more missing ones

Camille Landesvatter and Paul C. Bauer randomly assigned smartphone respondents to answer nine open-ended survey questions either by typing or recording their voices. The final analytic groups contained 800 respondents in the text condition and 661 in the voice condition. Spoken answers were transcribed with Whisper.

Among people who answered, voice performed well. Spoken responses were significantly longer for five of the nine questions, with differences ranging from 2.2 to 4.4 words. The authors also use response entropy, a measure of lexical information, and find a smaller advantage for voice there. The presence of other people during the survey reduced response entropy for voice answers on three items.

The missing-data result changes how I read the paper. Across the nine open-ended items, an average of 47 per cent of respondents in the voice condition supplied an answer, compared with 99 per cent in the text condition. Break-off was also concentrated in the voice arm: 204 cases against 42 in the text arm. The information analysis is therefore conditional on somebody agreeing to record an answer.

That distinction matters for development surveys. Voice entry could reduce the burden of typing for respondents using phones, particularly where scripts, literacy or device familiarity make text entry cumbersome. Yet a response mode that produces richer material from a much smaller subset can worsen total data quality. Privacy is likely to matter too. Recording an answer about household finances, violence, health or political attitudes while other people are nearby is a different measurement situation from typing it.

Landesvatter, Camille, and Paul C. Bauer. 2026. “Information Content in Text and Voice Response Formats for Open-Ended Survey Questions.” *Journal of Survey Statistics and Methodology*, smag030. DOI: 10.1093/jssam/smag030. Published 17 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article/doi/10.1093/jssam/smag030/8812674?utm_source=chatgpt.com)

Worth reading. The response-rate result is at least as interesting as the result on answer length.

## 2. SMS reminders bring respondents in quickly, while consent to receive them is selective

Eric Stone, Renee Stepler and Casey Eggleston use the US Census Household Panel to examine SMS invitations and reminders. Their September working paper uses survey responses and paradata from the May 2024 topical, which had approximately 10,000 respondents.

Responses rose in the hours immediately after text messages were sent. Around half of panel members consented to receive survey texts. Consent varied by race and ethnicity, age, family income, education, marital status, region and respondent type. The route respondents used to enter the survey also differed across demographic groups.

The lesson for CATI and longitudinal studies is fairly practical. Adding SMS may increase response while changing the composition of respondents reached through that channel. If SMS reminders become part of a mixed-mode protocol, the relevant paradata include consent, delivery, click-through and eventual completion by contact mode.

The paper examines an established US probability panel whose members had already supplied mobile numbers. Consent and response behaviour could look quite different in a newly recruited panel, or where phones are shared within households. I would want that tested before carrying the findings into South Asian surveys.

Stone, Eric, Renee Stepler, and Casey Eggleston. 2026. “Evaluating Text Messaging as a Contact Strategy and Predictors of Text Message Consent: Evidence from the Census Household Panel.” US Census Bureau, Research and Methodology Directorate Working Paper RSM2026-09. September 2026.

[Read the working paper](https://www.census.gov/library/working-papers/2026/adrm/rsm2026-09.html?utm_source=chatgpt.com)

Worth reading if you run panels or repeated phone surveys.

[Subscribe now](https://varna.substack.com/subscribe?)

## 3. small-area estimation gets a useful mixed-effects gradient boosting estimator

Paul Messer and Timo Schmid propose Mixed Effect Gradient Boosting, or MEGB, for unit-level small-area estimation. The method combines gradient boosting with random effects, allowing nonlinearities and interactions while accounting for dependence among observations within areas. They pair the estimator with a nonparametric bootstrap for estimating mean squared error.

The paper has both model-based simulations and a design-based application using household income data from Chihuahua, Mexico. The population dataset contains 58,578 households in 67 municipalities. Repeated survey samples contain 1,280 households from 22 municipalities, leaving 45 municipalities completely unsampled. The design-based exercise uses 500 Monte Carlo repetitions.

MEGB does particularly well when the underlying relationship is nonlinear and when within-area dependence matters. Its advantage becomes small under some low signal-to-noise settings. That qualification is useful. A machine-learning estimator does not automatically buy much when the available predictors contain little information.

There is another practical constraint. Unit-level auxiliary covariates are required for the entire population. Aggregated area-level covariates cannot simply replace them because the fitted function is nonlinear. That requirement may rule the method out in precisely the settings where researchers most want small-area estimates.

The present application estimates a continuous mean. The authors leave binary and count outcomes, poverty headcounts and inequality measures for later work. For development researchers, those extensions will determine much of the method’s practical value.

Messer, Paul, and Timo Schmid. 2026. “Gradient Boosting for Hierarchical Data in Small Area Estimation.” *Statistics and Computing* 36: 218. DOI: 10.1007/s11222-026-10970-1. Published 17 September 2026.

[Read the open-access paper](https://link.springer.com/article/10.1007/s11222-026-10970-1?utm_source=chatgpt.com)

Worth reading for researchers producing district or subdistrict estimates. I would wait for evidence on poverty and other nonlinear indicators before treating it as a general replacement for established SAE estimators.

## 4. one we missed: can satellite rooftops replace household listing in India?

Douglas Johnson and colleagues at IDinsight address an expensive part of conventional area-probability sampling. Once primary sampling units have been selected, survey teams often list every household before drawing the household sample. Where no current frame exists, listing can consume a substantial share of fieldwork time and money.

Their alternative is rooftop sampling. Researchers sample rooftops from open-source building datasets created by Google and Microsoft and use them to reach households directly. The paper develops a framework for assessing bias and tests the approach using Demographic and Health Survey data, an Indian ground-truth dataset and field tests.

The authors estimate that the approach introduces bias of around one percentage point for a binary outcome in their tests. Their cost analysis suggests that rooftop sampling can make sense for surveys with fewer than about 1,000 respondents and where conventional listing is infeasible.

This is one of the more directly useful survey-design papers for India this year. The attraction is obvious in rapidly changing peri-urban settlements and places where existing frames are poor.

The method moves several errors into new places. A roof need not correspond to one household. Buildings may contain several households, no household, or structures the building dataset failed to detect. Coverage quality may vary geographically. Those errors need local assessment before a rooftop frame can be treated as an adequate substitute for listing.

Johnson, Douglas, Anjani Balu, Poornima Ramesh, Linh Vo, Rediet Mulu, and Amir Emami. 2026. “Assessing the Reliability of Household Sampling Using Rooftop Data in India.” *Journal of Survey Statistics and Methodology*, smag019. DOI: 10.1093/jssam/smag019. Published 20 August 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag019/8767409?utm_source=chatgpt.com)

Worth reading. For Indian household-survey teams, I would put this ahead of most of this week’s papers.

Research Rundown should return to this one. I would like to see evidence on how rooftop sampling performs across dense informal settlements, multi-storey urban housing, tribal settlements and dispersed rural habitations. A national average bias estimate cannot answer that question.

[Subscribe now](https://varna.substack.com/subscribe?)

## 5. one more from August: predicting question reliability and validity before fieldwork

Barbara Felderer, Lydia Repke, Wiebke Weber, Jonas Schweisthal and Ludwig Bothmann update the Survey Quality Predictor, an open-access system that predicts the reliability and validity of survey questions from their formal characteristics.

SQP is based on a database of multitrait-multimethod experiments in which question characteristics vary. For SQP 3.0, the authors compare LASSO, elastic net, boosting and random forest models. Random forest produced the best predictions and became the new prediction engine. The paper also examines which item characteristics contribute most to predictions.

There is a useful role for this during questionnaire development. Researchers can inspect question form, response categories, labels and other design decisions before an instrument reaches cognitive testing or a pilot.

I would keep the claim narrow. SQP predicts quality from relationships learned in its existing MTMM database. It cannot establish that a translated item measures the intended construct among a particular population in Bihar, Bangladesh or Nepal. Local cognitive testing, measurement-invariance work and criterion validation answer different questions.

Felderer, Barbara, Lydia Repke, Wiebke Weber, Jonas Schweisthal, and Ludwig Bothmann. 2026. “Predicting the Validity and Reliability of Survey Questions.” *Survey Research Methods* 20(2): 133–145. DOI: 10.18148/srm/2026.v20i2.8453. Published 10 August 2026.

[Read the open-access paper and replication files](https://ojs.ub.uni-konstanz.de/srm/article/view/8453?utm_source=chatgpt.com)

Worth using as a diagnostic during questionnaire design. I would resist presenting its predicted score as validation.

## what I would read

The voice experiment is the best new measurement paper this week because its awkward result is the useful one. Voice yields richer answers among respondents who answer, while many more people decline to answer at all.

For field research in South Asia, Johnson et al. is more consequential. Household listing is expensive enough that a credible alternative deserves testing. The unresolved issue is heterogeneity in coverage error across settlement types.

Messer and Schmid is the technically strongest new quantitative paper. Its immediate use is narrower because full-population unit-level auxiliary data are a demanding input.

[Subscribe now](https://varna.substack.com/subscribe?)

## a question for readers

If you have tested satellite or map-based household sampling in South Asia, what happened when a sampled building contained several households, was vacant, or did not appear correctly in the building layer? I am particularly interested in field evidence comparing those errors with errors found during conventional household listing.

That is a question I would like Research Rundown to return to with actual field protocols and validation data rather than treating rooftop sampling as a solved replacement for listing.

[Share](https://varna.substack.com/p/methods-monday-21-september-2026?utm_source=substack&utm_medium=email&utm_content=share&action=share)

##

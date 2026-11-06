---
title: "Methods Monday | 28 September 2026"
date: 2026-10-01
type: other
url: https://varna.substack.com/p/methods-monday-28-september-2026
subtitle: "Interviewers, recall, probability scales and sampling designs, and the small choices that change what surveys measure."
source: varna.substack.com, fetched by scripts/sync_substack.py
---

# Methods Monday | 28 September 2026

*2026-10-01. Published at [https://varna.substack.com/p/methods-monday-28-september-2026](https://varna.substack.com/p/methods-monday-28-september-2026). This file is a generated copy; the Substack post is the original.*

[![Editorial illustration for Methods Monday showing a household questionnaire with Hindi translation notes, interviewer probes, a probability scale, sampling-frame sheet, field notebook, map and magnifying glass.](https://substackcdn.com/image/fetch/$s_!scDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78a82638-8080-4c78-95d5-84db8abafc51_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!scDM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78a82638-8080-4c78-95d5-84db8abafc51_1536x1024.png)
*Methods Monday on 28th September, 2026*

### What interviewers change, what questionnaires create, and when prediction should enter sampling

Last Monday’s voice-response paper asked what changes when respondents speak rather than type. Two papers published on 25 September take the next step: once speech becomes an interviewer-administered exchange, the interviewer and the question both enter the measurement process.

## 1. Some questions make interviewers depart from the script

Rodney Terry, Erica Yu and Holly Fee use wave 1 of the 2014 US Survey of Income and Program Participation to examine when interviewers rephrase questions or probe respondents. Their data combine computer audio-recorded interviews, interviewer observations and responses collected during the household interview.

Question characteristics were the strongest predictors of interviewer behaviour. Information interviewers acquired during the visit, including observations made at the doorstep and answers given earlier in the interview, contributed somewhat to later deviations, although the evidence for those effects was limited.

This shifts part of the quality-control problem back to instrument design. If the same item repeatedly produces clarification, probing or rewording, another round of interviewer instruction may leave the source of the problem untouched. The item itself may be difficult to administer as written.

That matters even more in multilingual South Asian fieldwork. An interviewer who has to translate an awkward phrase, explain an unfamiliar response category or decide what a concept means in a local language is making measurement decisions in real time. The US evidence does not tell us how large those effects are in multilingual CAPI surveys. It gives a good reason to measure them.

Terry, Rodney L., Erica C. Yu, and Holly Fee. 2026. “What Informs Interviewer Question Asking and Probing? Evidence from the Survey of Income and Program Participation.” *Journal of Survey Statistics and Methodology*, smag012. DOI: 10.1093/jssam/smag012. Published 25 September 2026.

[Read the paper and supplementary material](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag012/8836145?utm_source=chatgpt.com)

I would read this first if you run interviewer-administered surveys.

[Subscribe now](https://varna.substack.com/subscribe?)

## 2. Recorded interviews can be turned into usable survey paradata at scale

Hanyu Sun, Brad Edwards and Ting Yan use computer-assisted recorded interviewing and machine-learning tools to compare interviewer-respondent interactions across telephone, face-to-face and video interviews in a large US household survey. The system transcribes question-level recordings and derives measures of interviewer behaviour and respondent difficulty.

They examine whether interviewers read questions verbatim, whether they preserve the intended meaning, how many speaking turns respondents need, and how long respondent speech lasts. Differences across modes exist, but they are generally small. The larger source of variation is the question being asked.

That is the useful finding. Mode gets enormous attention in mixed-mode survey design. A badly functioning question can create more variation in interview interaction than whether the interview happens by video, telephone or in person.

The paper also demonstrates a practical quality-control method. Audio monitoring is usually expensive because somebody has to listen and code. Automated transcription and classification can make question-level review possible across far more interviews. I would still want human validation before using automated coding for interviewer assessment, especially across accents and languages that speech-recognition systems handle unevenly.

Sun, Hanyu, Brad Edwards, and Ting Yan. 2026. “Using Recordings of Survey Interviews and Machine Learning to Evaluate Differences in Interviewer–Respondent Interactions Between Telephone, In-Person, and Video Interviews.” *Journal of Survey Statistics and Methodology*, smag026. DOI: 10.1093/jssam/smag026. Published 25 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag026/8836143?utm_source=chatgpt.com)

Worth reading alongside Terry et al. The two papers make a fairly persuasive case for treating interview recordings as instrument-diagnostic data rather than material used only to police interviewers.

## 3. Auxiliary predictions can be used before sampling begins

P. García-Segador and P. Miranda ask whether predicted values of the outcome can be used to construct a better fixed-size probability sample.

The ideal sampling design would depend on the true values of the study variable, which are unavailable before data collection. Their method substitutes predictions generated from auxiliary information, including predictions from statistical or machine-learning models, and builds the sampling design around those values.

In simulations, designs based on imperfect predictions remained close to designs constructed using the true outcome values. They also produced lower estimation error than comparison approaches including cube sampling and conditional Poisson sampling.

The development-research application is clearest where sampling frames are already rich. Administrative registers, census variables, previous survey waves, satellite measures or programme data may predict the target outcome well enough to influence inclusion probabilities.

The risk sits in the predictive model. Relationships learned from old data may change. Administrative variables can contain their own selection and measurement errors. A complex prediction-based sample also requires unusually careful documentation if analysts are expected to reconstruct inclusion probabilities later.

García-Segador, P., and P. Miranda. 2026. “Conditional Optimal Sampling: Enhancing Unequal-Probability Designs with Auxiliary Information.” *Journal of Survey Statistics and Methodology*, smag027. DOI: 10.1093/jssam/smag027. Published 23 September 2026.

[Read the paper and supplementary material](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag027/8830419?utm_source=chatgpt.com)

Worth reading for survey statisticians and teams working with administrative or geospatial sampling frames. I would want field applications before using it as a routine design choice.

[Subscribe now](https://varna.substack.com/subscribe?)

## 4. In urban India, measured harassment prevalence depends on how the questionnaire asks respondents to remember

Lori Beaman, Seema Jayachandran and Anisha Sharma surveyed more than 4,000 women recruited in public spaces in New Delhi and Bengaluru. Their substantive study examines harassment and women’s use of public space. The measurement result deserves separate attention here.

Reported past-year harassment prevalence was 65 per cent in New Delhi and 29 per cent in Bengaluru. For groping, stalking or sexual assault, the corresponding figures were 41 and 14 per cent. The authors then show that measured prevalence is more sensitive to questionnaire design where harassment is less common and where respondents have fewer or less recent incidents available for recall.

That complicates cross-place comparisons. Retrieval from memory is part of the measurement process. Where an experience is frequent and recent, alternative prompts may produce similar answers. Where it is uncommon or distant, wording and recall structure can move the estimate more.

The result applies well beyond harassment surveys. Researchers measuring discrimination, illness episodes, shocks, violence, informal payments or service failures face the same recall problem. A prevalence estimate may partly reflect how hard the questionnaire makes respondents search their memories.

The paper is a substantive development-economics study, so the measurement experiment is narrower than a dedicated survey-methods study. That is also what makes it useful. These problems turn up inside ordinary empirical research.

Beaman, Lori A., Seema Jayachandran, and Anisha Sharma. 2026. “The City Through Her Eyes: Gender-Based Harassment in Public Spaces in Urban India.” NBER Working Paper 35738. DOI: 10.3386/w35738. September 2026. The NBER version was posted on 15 September and revised on 21 September.

[Read the NBER paper](https://www.nber.org/papers/w35738?utm_source=chatgpt.com)

This is the regional paper I would keep. Its measurement result has uses far beyond the subject of the study.

## 5. A respondent choosing 0 or 100 per cent may be telling us about the questionnaire

Carola Binder, Laura Crespo, Carlos Gento, Luis M. Guirola and Ernesto Villanueva examine probability questions used to measure subjective expectations. Respondents frequently put all probability on one outcome, which researchers often interpret as certainty.

Using the online ECB Consumer Expectations Survey and the interviewer-administered Spanish Survey of Household Finances, the authors find that this bunching is partly produced by the survey process. It occurs more frequently among respondents with lower financial literacy and increases with panel tenure.

Two changes provide stronger evidence. Standardising interviewer behaviour reduced bunching by about 15 percentage points. A later questionnaire redesign reduced it by another 18 percentage points. Variation across interviewers also fell following standardisation.

The development-research relevance is easy to see. Probability elicitation is increasingly used for expectations about rainfall, income, migration, employment, crop yields and shocks. Responses of 0 and 100 are tempting to interpret substantively. Some may instead reflect numeracy, task burden or the way an interviewer explains the scale.

The exact effect sizes should stay in their original setting. These are European surveys. The measurement issue could be larger where percentage probabilities are unfamiliar.

Binder, Carola, Laura Crespo, Carlos Gento, Luis M. Guirola, and Ernesto Villanueva. 2026. “(Mis)measuring Uncertainty: Bunching in Probabilistic Expectations.” NBER Working Paper 35733. DOI: 10.3386/w35733. September 2026.

[Read the NBER paper](https://www.nber.org/papers/w35733?utm_source=chatgpt.com)

Worth reading if your questionnaire contains expectations or probability modules.

[Subscribe now](https://varna.substack.com/subscribe?)

## 6. A large lottery did little to recover disengaged panel respondents

Rasmus Patton, Jannes Jacobsen, Jörg Dollmann and Almuth Lietz test whether a high-value lottery can bring respondents back into a quarterly probability-based online panel.

Participants were randomly assigned to the standard €10 incentive, the €10 payment plus a lottery offering ten €500 Amazon vouchers, or a conditional version in which continued participation increased the probability of winning. Neither additional treatment produced a statistically significant increase in participation. Subgroup analyses by earlier participation, education, income and country of origin produced no systematic effects either.

This is a useful null result. Attrition strategies often assume that respondents who have stopped participating require a stronger financial inducement. The experiment suggests that disengagement may have causes that money alone does not address.

Its relevance to South Asian longitudinal surveys is limited by context. A German online panel already paying €10 is far removed from household panels where attrition comes from migration, phone-number turnover, interviewer continuity, seasonal work or difficulty relocating households.

Patton, Rasmus, Jannes Jacobsen, Jörg Dollmann, and Almuth Lietz. 2026. “Motivating The Unmotivated? Testing Conditional Lottery Incentives in an Ongoing Panel Survey.” *Journal of Survey Statistics and Methodology*, smag035. DOI: 10.1093/jssam/smag035. Published 25 September 2026.

[Read the paper](https://academic.oup.com/jssam/advance-article-abstract/doi/10.1093/jssam/smag035/8836144?utm_source=chatgpt.com)

Worth reading for panel managers. The null finding is more useful than another small positive incentive effect would have been.

## What I would read

Terry, Yu and Fee first. Their result gives field teams something concrete to test: whether interviewer deviations concentrate in particular questions.

The India paper by Beaman, Jayachandran and Sharma is the measurement result I would carry into substantive development research. Recall is part of the estimator long before anyone runs

[Share](https://varna.substack.com/p/methods-monday-28-september-2026?utm_source=substack&utm_medium=email&utm_content=share&action=share)

---
title: "Research Rundown: Friday Findings -1 October 2026"
date: 2026-10-01
type: edition
url: https://varna.substack.com/p/research-rundown-friday-findings-632
subtitle: "Coal, drought and pregnancy, tribal representation, programme data, and the thin evidence behind urban climate-health action."
source: varna.substack.com, fetched by scripts/sync_substack.py
---

# Research Rundown: Friday Findings -1 October 2026

*2026-10-01. Published at [https://varna.substack.com/p/research-rundown-friday-findings-632](https://varna.substack.com/p/research-rundown-friday-findings-632). This file is a generated copy; the Substack post is the original.*

[![Research Rundown Friday Findings cover for 1 October 2026, showing a research desk with charts on changing sources of urban air pollution, drought and pregnancy outcomes, tribal representation and forest conservation, urban climate-health evidence, and a programme data-to-decision flow.](https://substackcdn.com/image/fetch/$s_!_1X-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a630746-318c-489e-b45c-209c6fb9d864_1672x941.png)](https://substackcdn.com/image/fetch/$s_!_1X-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a630746-318c-489e-b45c-209c6fb9d864_1672x941.png)
*Friday Findings for 1st October 2026*

### programming note

Friday Findings is arriving a day early this week. Friday, 2 October, is reserved for a Research Rundown Gandhi Jayanti special. The research window here remains the usual seven days, 25 September to 1 October.

### coal, drought and pregnancy, tribal representation, programme data, and what we actually know about climate action in cities

This is a compact issue. Two new peer-reviewed papers on India deserve close attention. One links electricity demand and coal generation to the changing composition of urban air pollution. The other links district-level drought exposure to preterm birth and low birth weight, although a serious survey-design problem tempers the result. A Chhattisgarh study asks whether the level at which Scheduled Tribe political representation occurs affects forest conservation. Two further pieces are worth keeping for methods and implementation.

My bias this week is toward work where the design teaches us something beyond the headline result.

## 1. India’s economic boom changed the composition of its air-pollution problem

Swain, Basudev, Aishwarya Singh, Debashis Tripathy, Rui Song, Adrien Deroubaix, Marco Vountas, Pritanjali Shende, Chenchen Huang, Luca Lelli, and Ankit Tandon. 2026. “Economic-boom-driven electricity demand linked to urban air pollution and health in India.” *Nature Cities*. Published 25 September 2026. DOI: 10.1038/s44284-026-00518-9.

This is my pick of the week.

Between 2000 and 2020, India’s GDP per capita roughly tripled while electricity demand rose almost fourfold. Coal supplied about 76% of generation. Over the same period, the authors estimate that urban aerosol loading doubled and sulfate came to account for about 46% of that burden. Estimated urban PM2.5-attributable deaths rose from roughly 0.7 million to 0.9 million. Household air-pollution mortality, meanwhile, fell as clean-cooking access expanded.

The paper earns attention because it separates sources rather than treating PM2.5 as a single exposure. The authors combine MERRA-2 reanalysis, MODIS MAIAC satellite observations, GEOS-Chem atmospheric modelling, TROPOMI SO2 observations and Central Pollution Control Board measurements. GEOS-Chem attributes a growing share of urban aerosol loading to the power sector, whose estimated contribution to total urban aerosol optical depth rises from around 16% in 2000 to 36% in 2020.

The causal language needs discipline. Economic growth, coal generation, urbanisation and pollution changed together over two decades. Atmospheric source-attribution models can identify plausible sectoral contributions with considerable sophistication. They do not turn the historical association between GDP growth and mortality into a clean causal estimate of the health cost of growth.

The mortality numbers also come from comparative risk assessment using Global Burden of Disease estimates. They are modelled population burdens, with uncertainty in exposure, risk functions and baseline mortality.

The result I would keep is narrower and more useful. India’s move away from household solid-fuel exposure has coincided with an increasingly electricity-linked urban pollution burden. Public-health policy therefore has to follow the energy system as exposure shifts outdoors.

[Read the open-access paper](https://doi.org/10.1038/s44284-026-00518-9?utm_source=chatgpt.com)

[Subscribe now](https://varna.substack.com/subscribe?)

## 2. Drought exposure is associated with preterm birth and low birth weight. The design deserves scrutiny.

Bhattacharjee, Sujayita, Arup Jana, and Aparajita Chattopadhyay. 2026. “Drought assessment and linkages with selected pregnancy outcomes in India using satellite-based aridity analysis and large-scale data, 2019–2021.” *Discover Public Health* 23: 1524. Published 25 September 2026. DOI: 10.1186/s12982-026-02694-4.

This paper links MODIS-derived aridity measures with NFHS-5 data. The analyses cover 148,746 institutional births for preterm birth, 232,920 children with recorded birth weight, and pregnancy histories from 724,115 women. Around 43.7% of the study population was classified as drought-exposed.

After adjustment, drought exposure was associated with 12% higher odds of preterm birth and 8% higher odds of low birth weight. The adjusted miscarriage association was effectively null.

The sample size is impressive. The inference is weaker than the N suggests.

The authors explicitly state that their analyses do not incorporate NFHS sampling weights, primary-sampling-unit clustering or stratification. For a complex national household survey, that is a substantial limitation.

Exposure measurement adds another problem. District-level drought conditions are attached to pregnancy outcomes without precise gestational timing. A woman classified as drought-exposed may therefore have experienced a different exposure window from the one biologically relevant to the outcome.

I would read the paper as evidence of a spatial association worth pursuing. A stronger design would use more precise temporal exposure assignment and respect the NFHS survey design.

This is an obvious Methods Monday candidate. Large N does very little to rescue a mismatch between sampling design, exposure construction and the inferential claim.

[Read the open-access paper](https://doi.org/10.1186/s12982-026-02694-4?utm_source=chatgpt.com)

## 3. Tribal political representation appears to conserve forests when the office carries enough authority

Agarwal, Bina, Shamindra Nath Roy, and Shiva Chakravarti Sharma. 2026. “Forest conservation and indigenous political reservation: What level of representation is effective?” *Ideas for India*, 29 September 2026. The article reports findings from the authors’ 2026 *World Development* study of Chhattisgarh.

This is a new public-facing analysis of research published earlier this year, so I am treating it as substantive new analysis rather than a newly published underlying paper.

The study uses satellite-derived forest-cover data and GIS mapping across roughly 20,000 Chhattisgarh villages from 2001 to 2019. It separates villages into seven categories according to whether Scheduled Tribe representation applied at assembly-constituency level, through PESA village councils, through both, or through neither. The authors then estimate panel, OLS and logistic regressions with controls for population change, cultivation dependence, roads, proximity to towns, nearby forests, poverty and baseline forest cover.

Villages that experienced some form of ST reservation gained an average 22.71 hectares of forest cover over 2001–2019, compared with 5.38 hectares among never-reserved villages. The disaggregated result matters more: villages with sustained assembly-level reservation performed better, while villages covered solely by PESA did poorly.

The authors interpret this through institutional authority. MLAs control discretionary funds and have greater access to the bureaucracy. ST sarpanches operate with fewer resources, mixed local electorates and, during much of the study period, weak implementation of PESA’s forest powers.

This is much more interesting than a simple “representation improves conservation” claim. The study suggests that the administrative level at which representation occurs may determine whether political voice can alter an environmental outcome.

Selection into reserved areas and the policy changes surrounding the 2008 delimitation still complicate causal interpretation. The authors deal with these institutional changes explicitly and test several specifications, but the design remains observational.

For work on decentralisation, tribal governance or community natural-resource management, this one deserves a full read.

[Read the open-access Ideas for India analysis](https://www.ideasforindia.in/topics/environment/forest-conservation-and-indigenous-political-reservation-what-level-of-representation-is-effective?utm_source=chatgpt.com)

[Subscribe now](https://varna.substack.com/subscribe?)

## 4. Large livelihood programmes collect enormous amounts of data. The harder question is whether anybody uses it.

Das, Kumar, and Neha Dhingra. 2026. “Unlocking the power of administrative data to strengthen programme delivery.” *Ideas for India*, 28 September 2026.

This is an implementation piece rather than an evaluation, but I am including it because the problem will be familiar to anyone who has worked with a large government MEL system.

Das and Dhingra use Samaveshi Aajeevika Yojana, the Ministry of Rural Development’s economic-inclusion programme for ultra-poor and marginalised rural households, to examine what happens to administrative data as a programme scales. SAY generates data through participant identification, household profiling, livelihood plans, coaching visits, financial transactions and convergence with government schemes.

Their argument is that the binding constraint increasingly lies in governance around data use: who interprets an emerging pattern, who has authority to act on it, and whether information travels back to frontline staff. The authors also warn that linking incentives too tightly to reported indicators can shift staff behaviour towards target achievement.

There is no impact estimate here. The article does not show that a particular administrative-data system improves programme outcomes. It gives a management diagnosis and a set of design propositions.

I would still keep it. Development programmes spend heavily on MIS platforms and dashboards while giving much less attention to the decision rule attached to each indicator. A dashboard that generates no specified action is mostly a display.

This has a direct connection to our recurring Methods Monday discussion about measurement systems. The next useful step would be empirical: identify cases where changing the feedback architecture of programme data altered implementation quality or participant outcomes.

[Read the open-access analysis](https://www.ideasforindia.in/topics/governance/unlocking-the-power-of-administrative-data-to-strengthen-programme-delivery)

## 5. The evidence for city climate-health action is much thinner than the rhetoric

Hutchinson, Emma, Tobias Magnus Schuster, Melanie Crane, James Milner, Kristine Belesova, Roberto Picetti, Simon Lloyd, Catalina Turcu, Jane Falconer, Blanca Anton, et al. 2026. “Systematic overview of climate actions for health in cities.” *Nature Cities*. Published 29 September 2026. DOI: 10.1038/s44284-026-00515-y.

This review is global. I am making room for it because Indian cities are rapidly adopting climate, clean-air, mobility and heat interventions, while evidence of health effect often comes from a much narrower set of settings.

The authors screened 5,550 records, critically appraised 60 systematic reviews and retained 49 whose findings met their confidence threshold. Most evidence concerned transport, urban form and buildings. Fifty reviews drew on studies from high- or middle-income countries; only ten contained information from low-income settings.

The quality assessment is sobering. Only six of the 60 reviews received medium or high confidence ratings. Seven reviews, about 12%, meta-analysed effects. Evidence on food and waste interventions was particularly sparse, and only seven of the 49 included reviews examined implementation barriers or enablers.

The literature is strongest around active transport and housing improvements. Evidence on city-wide, cross-sector programmes capable of producing large climate and health gains is absent from the published review base the authors examined.

That does not establish that integrated urban climate programmes fail. It tells us that the evaluation literature has not caught up with the claims being made for them.

This connects directly with the WRI India road-dust and open-waste-burning papers in the 18 September Friday Findings. Those studies were useful precisely because they measured specific sources and interventions. This review explains why that apparently mundane work matters.

[Read the open-access paper](https://doi.org/10.1038/s44284-026-00515-y?utm_source=chatgpt.com)

[Subscribe now](https://varna.substack.com/subscribe?)

## What I would keep

Swain et al. is the week’s strongest substantive paper. The source-attribution work gives a more useful account of India’s changing pollution burden than another national PM2.5 trend.

Bhattacharjee et al. is the paper I would use in a methods classroom. The very large NFHS sample makes the unmodelled survey design easier to miss, which is precisely why it is instructive.

The Agarwal, Roy and Sharma study raises the most interesting political-economy question: whether representation changes outcomes only when the represented office has enough fiscal and administrative authority to act.

The urban climate-health review supplies the corrective. We have many plausible mechanisms and policy proposals. Evidence from implemented, cross-sector city programmes remains sparse.

I found several new nutrition and public-health papers during the search that I have left out. One Indian child-obesity study, for example, drew its sample from 163 children in a single affluent private school. It is too narrow for Friday Findings. I also found current Bangladesh and Pakistan commentary on macroeconomics and climate finance, but little new empirical work within the seven-day window that justified adding items simply for geographic balance.

## For readers

I am looking for South Asian evaluations in which routine programme or administrative data were actually used to trigger a management change, with evidence on whether that change altered delivery or participant outcomes. If you know one, send it across. Reader recommendations that make a future Friday Findings will be credited.

[Share](https://varna.substack.com/p/research-rundown-friday-findings-632?utm_source=substack&utm_medium=email&utm_content=share&action=share)

##

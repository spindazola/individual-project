Oct 13, 2026

## Meeting Oct 13, 2026 at 13:09 BST - Transcript

### 00:00:01



Um yeah, I think this video will be useful to catch up on how things how you're seeing things from your side, how you're getting on with this new explosion of ideas that you're looking at. Yeah. Um and I also wanted to give this to you which is what I promise you. Y um so take good care of it.





### 00:00:24



Yeah. And it has the full checks per data set on it. So tell your German explorer you will see essentially all the images. So you have the images on one side and then you have the CSVs with the labels. Yeah. Which is really important. Um yeah. So how how are things on your side?





### 00:00:46



Two things. Are we using the checkport data or are we using um our data that is um the one you told me regarding uh from the medical school. So we check which is the the free one the the free one. Right. Right. And the rational behind that is that it is a much more challenging process.





### 00:01:13



So the one that we were working with the hospital is mostly tabular data and it has some brain volumetrics extracted into them but essentially you don't work with images. Yeah. So my idea was to we get started with JAR we understand that and then if we have time we add the the other things. Oh okay.





### 00:01:34



Because I've put in my in my brief I put um I didn't put checks but yeah don't worry. Um yeah so I think that that's and check will give you the opportunity as well to you know because it's already it's already published and it's like it's like a like a stand for published data is a very prestigious so there's a lot of information about it as well so an advantage of that that you can read lots of paper usable so you want to understand and then you will have lots of resources um whereas the data that we have from the hospitals you





### 00:02:11



choose like a very there's nothing about it, right? It's just a data and then we we usually need some clinician advice to to actually get through it. Okay. So, I'm just going to read my project brief. So, we're just on if we're not on the same page, we iron it out right now. Okay.





### 00:02:27



Let's do it. Confirmal prediction. So, I've written my name. Marginal and condition specific reliability of confirmal prediction and chest X-ray classification is the name of my project title. Okay. Yeah. Happy. Yeah. Okay. problem. Conformal prediction provides prediction sets with a specific specified marginal coverage guarantee.





### 00:02:48



For example, a 90% predictor should contain a true class approximately 90% of the time. Mhm. However, this guarantee holds across the data overall and does not ensure show 90% coverage for each individual class. In chest X-ray classification, where conditions differ in prevalence and difficulty, good overall coverage could therefore conceal substantial undercarbage for partial conditions. Okay.





### 00:03:14



Furthermore, practical CP requires choices concerning calibration data, data splitting, and conformity measures. This project will investigate how these choices affect the reliability and reproducibility of conformal coverage with particular emphasis in differences between marginal and condition specific linkage. Yeah, perfectly good. Here are my goals. Develop a reproducible single label classification for 10 x-ray conditions.





### 00:03:47



So, I said 10. I wasn't sure if that was the right number. Oh, that's right. Using two to three relatively simple classifiers. So that's an initial goal. Then implement split confirmal prediction and verify its nominal marginal coverage. Then measure and compare condition specific coverage investigating whether overall coverage conceals under coverage for particular or less prevalent conditions.





### 00:04:13



Mhm. Then compare calibration strategies including different sources, provenence of calibration data and data splits. Then investigate suitability conformity measures and quantify their effect on coverage and prediction set size. Yeah. Then finally repeat experiments where appropriate to assess the stability and reproducibility of observed results. And then here's my scope. This project will focus on uncertainty quantification rather than maximizing classifier performance.





### 00:04:49



The classifiers are intended as controlled experimental distribution free and quantification. Okay. The classifiers are intended as controlled experimental models rather than the state-of-the-art diagnostic systems. Yeah. The initial investigation will use a simplified single label multiclass formula formulation. This is what we discussed. initially do single then if we get time yeah then a more complex multi multi- label problem will remain as a possible ex extension if time permits the work will evaluate empirical condition specific coverage but will not claim full instance wise





### 00:05:26



conditional guarantees or clinical diagnostic validity yeah okay so that sounds very good so that's essentially what we discussed last time yeah I think you cultured quite Um I think a good thing to do for you now because you have read sufficiently on CP. Yeah. Um is to write a report on it. Yeah. Okay.





### 00:05:50



to an extended report in which so there are many things that you can do this with Um I'm not sure if I if I told you so the way I usually like to work with my students to make them write reports. Mhm. Right. Because then we put together your reports and then you have we keep aggregating reports and then you have your dissertation.





### 00:06:09



Yeah. And at the end of the day you would be editing rather than Yeah. You told me that like so discuss I'm working on report to assess my understanding of the first paper which is literally just a general introduction. So I'm two pages in I'm aiming for four pages just to yeah so remember you don't have to be exhaustive there just the main things that we are going to use in our research okay so essentially you talk about CP





### 00:06:38



um yeah so the report that you are writing is specifically on CP so you will write for example about definition you will write about and um coverage. Okay. And this is the marginal one. Okay. You will talk about how you can use split. Yep. Okay. So, split gives you cover and marginal and then conditional.





### 00:07:12



Conditional and then search to get important things that you have to say here. Um and the point we do this is so that you can learn to to write research as well. So there is a very good there's a very known a well known um impossibility result here. So true conditional coverage is actually impossible. You cannot get it but you can empirically approximate it.





### 00:07:44



Okay. So kind of empirical approximations to it is what we need to discuss here. What you will ultimately okay this itself that's like a beautiful report. Okay. And I'm pretty sure this report will going to transform it into a chapter in your thesis afterward. Now this is this is let's just call this report one.





### 00:08:15



to give it a minute. Um, my eraser. Oh, yeah. One second. Can I just Yeah, I keep writing. No worries. You can take eventually. Eventually, my goal is I will be writing and you will be correcting me. So in say maybe a month it should be me right now.





### 00:08:45



Yeah. Yeah. Yeah. I mean the expectation is that eventually you will get so into it into it that you will see the details that I will not be able to see because I'm working on this 247 like you will understand 247 but you know what I mean. No, I'm working hard. Yeah.





### 00:09:06



Um so the second one will be really useful for you is J. Okay. Yeah. So essentially you will write everything about the data because the data itself is much more complex than you would expect because it has machine learning built into it. It is lab system, right? So it has some very sophisticated NLP stuff to the problem.





### 00:09:27



Oh, NLP. That's a great thing. So, the problem with medical data is that it's very hard. Like doctors are very busy people and we cannot have them label like freaking 200,000 images, right? Yeah. So, what they did essentially they created an annotator like an NLP system multimodal really that went into what doctors write and diagnosis and so on.





### 00:09:57



but all from the doctor's notes and then it labelled images according to that. Yeah, it's very cool. And then they had a very small validation set where they actually made it um make those annotated and then they tested their the method, right? Yeah. Um so our report will be good like for example here you will get kind of the surrounding the literature surround surrounding like um medical ML.





### 00:10:30



Mhm. Then here you can ask questions like like what are we predicting here? And then you will see the kind of structure of the data. For example, you will see that you have like a different 14 possible disases. We're not going to look at the 14, but you have to discuss them anyway. Talk about the volume of the data, how it was annotated, and um what is really cool about this data set is that gives you and you don't see this in medical data.





### 00:11:05



It gives you a hierarchy of how labels relate to each other. Is it graphical or relational? graphical. Yeah. Yeah. So, no. So, so what what they give you is just like a tree like structor and then you can my my idea what we what I think we could do with you is kind of see how that structure kind of comes out on the prediction whether we can





### 00:11:30



say something. Yes. Because um so I read the checkexert one and I don't really understand it very well. Yeah. But it talked a bit about the hier hierarchical stuff and I was thinking um the way they do it like it's sort of like a knowledge craft sort of thing isn't it and the literature behind the structural when they start talking about knowledge because it's it's a very small footnote actually in a very small paragraph talking about the knowledge um knowledge graphs um





### 00:12:08



and then when they talk about that structure um through the hierarchy um surely when we talk about like now I'm thinking as a broader scope the whole project can I yeah you know when we talk about the 90% classification reliability right Yeah, here's my thing which I found really weird. Every single YouTube video I watched about this and I don't know if I should put YouTube as one of my sources.





### 00:12:43



I don't not yet. Yeah, just like understanding all of them use relational relational hierarchies. So you know X was then there's some data here like Excel table. Yeah. Surely like and I'm talking if we're trying to do something novel we exploit this. Yeah. So that that that is essentially what we ultimately want to do.





### 00:13:13



Okay. So because you don't it's very strange that in a data set you get that as an input. Yeah. Right. So because we know it beforehand. So let me I just wanted to show you the the the check is there. Uh is this this is a Samsung Galaxy Tab S9 whatever.





### 00:13:42



Um so you don't you use a laptop? I use a laptop but it's connected there in my I want to show you my desk actually. Um, yeah, I'm free all afternoon. So, I'm after this meeting, I'm just going to be doing my IP essentially. Cool. I have to see two more students.





### 00:13:59



That's fine. And then actually they have it. Yeah. So, they give you essentially Yeah, they give this. Yeah, that's what I was talking about. Yeah. Which is very strange. So but so that because we have that now it means that if we can kind of reconstruct or see or approximate it if we use some fancy CP um heristic here let's say to see to model





### 00:14:30



hierarchies and they see how much we are actually far away from this that would be very noble. Yeah right. Um but that is that is something that is ultimately right. So what I want us to do is to build onto that build step by step essentially because like to be to be honest this is kind of like a full research agenda that we can do be doing these things.





### 00:14:53



Yeah. Right. Again this is I want you to challenge me. Yeah. as I had said like I'm here to for you to like you know when you're washing curts you yeah so but in order to be able to squeeze you I need to make sure that you understood the basic things right and writing is the best way to do that so kind of going back on the shortterm stuff I think if let's say by next week we have some draft of this okay right and I'm talking draft I don't mean you should be comprehensive like it had to it doesn't have to be perfect or anything like that just a





### 00:15:33



draft like covering this having a discussion on this um and if you send me like before I meet you like for example yes that's fine then I'll be I will have time to read the to read and understand yeah okay that's absolutely fine yeah um another thing is can you just we were continuing about that because I don't want to we went off off track okay no yeah so this is report one so you will understand here and the tool the tool set that we're going to use the second thing is that





### 00:16:02



we need to understand the data very well right yeah because it has this chapter essentially what I want to what I want is to do venture I don't even know if it would be within this project we can actually extend something like publish something later is to kind of make a connection between this hierarchy and uncertainty okay yeah and quantify by that and this this link doesn't exist.





### 00:16:30



Okay. So if we can do something because I want to introduce you eventually at bowling. So we are working we are writing a paper with people from MIT actually. Um so we are define we are writing a theory in which we can hierarchy theoretically and create a hierarchy of uncertainty. The thing is that when let's say when you in traditional machine learning right you get a point prediction yeah and people give you the standard v the standard deviation for example yeah that is just like a very you don't know what when the certain is coming from there so when you use it you get like much





### 00:17:09



more insight because you get now the prediction set and you you get the the the width of the prediction set and so on so you get much more information here but still you don't know exactly how much of the of The uncertainty is epistemic which is exactly relates to how um to things that to reducible ignorance of your model.





### 00:17:33



That means if you do like a better job training your model that uncertainty can be reduced and then there is another kind of uncertainty that is called aluric. Alicuric uncertainty is some sort of irreducible noise that is always present in the universe to you cannot get rid of that. you can bound it but you can get rid of.





### 00:17:52



So essentially having a hierarchy of saying how much of this for example hierarchy that we see here of these probabilities here actually are explained by just some lack of knowledge from our model and how much of it actually just because of randomness of things. So it becomes more and more philosophical as you go up the level of abstraction let's say but we kind of like the whole um um research agenda is to hope or the karchical thing that we are working on now soon.





### 00:18:25



So my idea is to kind of get involved in that. I'm very interested in the hierarchical stuff that you just mentioned. Yeah. Um because yeah especially because I've big interest in graphical stuff. So yeah. So I think intellectually it's very challenging to to think about this especially um to distinguish where almost like epistemological questions.





### 00:18:49



You want to know like how much you can know and through um a machine learning system and how much is just like irreducible noise from the data itself. Yeah. So that's kind of the long the long form discussion but anyways again report I think you should just just focus on on checkpert itself. Yeah. And you will see that checkper has they either give you at for each this for each patient it tells you whether a condition is present is not present or is uncertain.





### 00:19:21



Yeah. Right. The uncertainty labels. So those uncertain labor thing at some point we need to study. Okay. Right. So here you can label types would be very nice to kind of um discuss. Okay. Okay. Okay. So, you have two reporting sessions now that you can start working on.





### 00:19:40



That's fine. Yeah. Yeah. Okay. So, this is the most important one now. And then after this one, you can do two. Okay. I didn't even think about doing report two. So, let's I'll focus on report one and then start think so to catch you up on what I've did done essentially since last week is you know the Jupyter notebook.





### 00:19:59



I tried to open the paper. Yeah. I tried to reproduce it essentially. Yeah, that's that's useful. How did you find it? Good. I think because it's settled into my head a little more, I'm understanding. Like before I feel like I was just chucked into it and it's like but now I'm like more Yeah.





### 00:20:17



I always say that your math cannot get through your fingers, right? So you have to you have to like you have to really like Yeah. marry it. Yeah. So um that's what I've been doing. And you see it's very it's very even ironical because if you see the C implementation it's like three or four lines.





### 00:20:35



Yeah. But to understand those three or four lines actually a lot of cognitive effort. Yeah. Even though in lines of code it's not um um right. So and then like I made a like a fourstep program of what I should be doing. Okay. over the next like I I made like a weekly goal.





### 00:21:00



So you told me to start thinking about GAN chart. Yeah. So I made like a basic GAN chart. Mhm. Um which I I intend to email to you just so that you are in the same Yeah. understanding of me. So you can start doing these things. Yes. So I make I I'll probably make a one drive and for the most part I want to let you know is I'm doing it in over leaf.





### 00:21:23



I'm using latex for my report. Share with me instead of word. Yeah. Um, so I can I mean that's much better otherwise like writing mathematics is it's awful. Yeah. So uh yeah, I can Yeah, there's a share button here. Oh, great. I can just send it to you.





### 00:21:46



But that's on my personal email if you don't care. Like my Latex account is my personal email address. Okay. Yeah. You you don't care. I don't care. And so here I can I just show you my stage like sorry when is your next deadline? Are you aware? It's kind of useless.





### 00:22:06



I sorry it's a bit of a useless deadline. I'll just show I I'll text the next deadline is I will leave you in charge of reminding me about your deadlines. Project plan and budget which is so project plan is due. So that's your guide 26th. Yeah of so in two weeks. Two weeks.





### 00:22:31



Yep. Again I've basically done this. I've written it already. Yeah. Um in fact here this is my project plan. Okay. Good. The only thing I wanted to ask you about was it says uh uh No, it doesn't. Not in this one. In one of the future ones, it asks you what um ask you about what like risk assessment.





### 00:23:01



So you have I have to talk about healthcare data. Oh yes. Yeah. And then this is a project budget. I don't think I need a budget. Yeah. Unless this comes. Yeah, probably not. Um I mean, do you actually have a budget that you can spend on this?





### 00:23:20



150\. So whether you get one and then you keep it. I I presume you keep the stuff that you buy or you have to return. You have to return it becomes university. Oh okay. Never mind. So I can send this to you just so you want to read through and then we have a risk assessment and data management.





### 00:23:37



That's an important one because how are you crying the data? Is it ethical format? All that sort of stuff. Good. Yeah. So in terms of next step let's talk my Okay. I have I have this weird question that I wanted to ask you. Yeah. Every project I've done through the universe, he has always been a project, a practical one where it's Right?





### 00:23:59



I'm going to build this. How am I going to build this? Or I'm going to test this. How am I going to test it? This is the first time I've ventured into the theoretical side. I don't really know how you start writing. Does that make sense? Yeah. Yes.





### 00:24:15



How you start writing in general? Like for a theoretical one. Mhm. Um, so I'm basing it off what you told me. Start reports and then eventually it will just come together. Yeah. That's the way to write. Okay. So there's no spectacular way of writing. It's just bits by bits.





### 00:24:33



Okay. And because look at this. So when when you write this, you will be forced to write the formal definition of a of what you know yeah a label space is a fixture spaces and so on. And then you will you will give me a theorem when you show me the coverage here and this. Okay.





### 00:24:52



And when you write that you need to understand it, right? It forces you to to kind of just maybe wait a bit, go to your notebook, write it down and kind of deduce yourself and then come back and write it. So you learn quite a lot about that. And then the other thing that I in case is not clear or obvious, put your references.





### 00:25:10



Okay? Right? References needs to be and this is usually the the most important feedback that I will give you. Everything that you say, you need to support it in research. If you don't give me a reference for a statement that you make that you can make I will I will challenge you on that because I will assume that it comes from you and not from someone else.





### 00:25:29



Okay. Right. So when you give me an statement just show me the literature and that actually strengthen quite a bit your your understanding. Okay. Yeah. And and what you had told me about like in these research papers there's research papers. Yes. So and then also I started finding my own ones.





### 00:25:45



Yeah. So I've I've put all in like an Excel file of what what I have save. You can have a look if you want to because you already started seeing quite a bit of papers. Yeah. You can a specific software to manage papers if you want like men is very good. Men like the scientist.





### 00:26:08



Yeah. 2GB free storage. Okay. That's great. Yeah. So you can use like um a give you a library and then you can export um latex style citation like bit bip text. Okay, great. Uh might be useful to you, right? So majorly because my goals for next week, my deliverable for next week, I will say report one.





### 00:26:44



Mhm. And then I want I want to send you my Jupiter notebook. So, I'm going to send a put it on my GitHub and then I'll send you the link. Yeah, I mean I'm I think we can do that later. So for now, keep your notebook for your own understanding. Okay. Um because the idea is that you all I mean you build as well some sort of independence, right?





### 00:27:15



So what I'm trying to do now is kind of put a thing into your mind and then through our discussion I want you to develop your own ideas and at some point like you said yourself. Yeah. So I want you to tell me if you have some question is say hey I found something in the literature and I'm curious about it but tell me right so we can because this is usually how how our be





### 00:27:39



my best project with students actually came out so the students actually find something and then you know we can pursue it if it makes sense. Yeah. And not saying it makes sense because the idea is not good enough or might be good or not good is because we have a constrained amount of time essentially. Yeah.





### 00:27:55



Um, so going back to what you said about the papers, read the papers and look at the references of the papers. Um, but be careful of not going everywhere in all places because there are so many of them. So make sure to select and discern which ones are actually fruitful for you because I I assure you that all of them are interesting, right?





### 00:28:23



Um but not all of them will be useful to you now. Yeah. So you could you could add in your mandate library like the one 10 papers that you say hey these are really the stuff. Right. Yeah. And then as you write those things then site them. Okay. Right.





### 00:28:43



And and and then each report is a snapshot of what your final thesis will be essentially. Okay. And that's how you write research. There's not there there's no shortcut. There's no shortcut. There's no shortcut. It's through the desert. That's it. Yeah. Um so I would say for next week if you give me a draft uh for report number one and then you start looking at the structure of the data that will be very good.





### 00:29:10



Okay. Yeah. And then once you know more about the structure of the data that will inform your thinking about Does that make sense? Yeah. Any questions? How do I Any figures you're expecting? Any graphs? Any pictures? Any I want I want to see how you write actually and then I can send your stuff.





### 00:29:39



Okay. Yeah. So I don't want to yeah I don't I don't I don't think working top down is very useful. So you want to just work and then see like bottom up that makes sense right? Okay. Um so if you when you are writing you see huh like this that would it would be really useful to show this in a graph do it.





### 00:30:03



If you think it'll be useful just do it and include it and then we can discuss it. Yeah. Right. Yeah. So remember like ultimately this is your work and if we let's say write a paper together afterwards you will be the leading author. Right. So that means it is your Yeah.





### 00:30:20



We shall see. No I'm not I'm not saying that that is something I expect de Valente. Yeah. What what what I'm saying is that no because it's not very strange. So no that is my goal. Yeah. My goal is to be published just like let's go a step don't put a lot of pressure on yourself either right because research it can go good and can I would say always go goes good but it not always goes as we want it to go.





### 00:30:47



So sometimes we find what we expect to find. Sometimes we find something completely different. Yeah. Uh but if that's true then we'll follow it. Right. Yeah. But I'm just saying that last year for example uh I don't think I can I haven't I can't introduce her to you now but my student she did a very good job on these ideas.





### 00:31:09



Yeah. And she published in Korea now in South Korea this year in a big conference. It was really good. Yeah. And now we're writing a journal paper again on because then she did her masters with me as well. So we work two years together and then we like three publications out of Okay.





### 00:31:26



Yeah. Um questions because I wanted to say this um actually no this is not what you asked me to do but this is what I wrote in my own GAN chart. I wanted to establish the interface interface um where I initially put like K equals 10. Okay. Because that's was like sort of a reasonable number.





### 00:31:53



Happy or what is K? Um K as in for like the number of as we had discussed in our project brief. Um check 10 X chest X-ray conditions essentially. Also also because number of classes. Okay. Yeah. And also because erggo and since I had based this off go. Yeah, they only supply 10. Yeah, I'm pretty sure 10 diseases is very good.





### 00:32:29



So if you look at the in the checks per web page that I showed you, there is a leaderboard of the competition. Um, do I get it? No. So it's not this one. It is this one. So this is a web page of the competition, right? And then you see the leaderboard here and these are this is what most machine learning paper stand.





### 00:32:55



Yeah. So they report the AOC, right? The AOC and then the one that reached the highest wins, which is freaking useless for doctors, right? So they don't care about one number. They just care how much they can actually trust it. So that's the main problem though. This is exactly why we do the things that we do.





### 00:33:16



But you will see that all of these people are actually giving a paper. You see this is an archive paper. This is an archive paper again and so on. So there's a lot of information about how people manage this data because when you're going to because eventually you will train models, right? Yeah. And you will need to know how you can process the pre-process the image, how to cut it, how to instantiate things and so on.





### 00:33:41



Yeah. So there's a lot of information on this, right? So this will come later. I think for your report number two, you can dive into these references and see how people were using this data set. Um and there is a criticism that we can make, right? So these are just they're reporting this one number, but a doctor wouldn't know here like what are the false positives like false negatives if okay I didn't why didn't I search this up?





### 00:34:09



Okay, great. Yeah. Um, yeah, I think that's pretty much it. We're good, I think. Yeah, I don't really have And so, let's agree to meet every Tuesday at this time in this place. So then we didn't have to negotiate every time. And also, it was Tuesdays that always worked for you, right?





### 00:34:37



because I had asked you about your Thursday availability and you said you know so Tuesday is better because I have this place. Yeah. And it's easier for me. Yeah. Because otherwise you have to hunt for Yeah. So what what I'm doing is I stacked all of you on Tuesdays. I have backtoback meetings.





### 00:34:52



Yeah. And calendar is starting to get crazy and I don't know why he doesn't see Cool. So yeah cuz um yeah so then I have Ashwin then and yeah so you're doing two third year projects and then two four year projects is that yeah so I just finished the master just submitted now so I was doing three of those and then three of you like undergraduates now three so me Ashman and yeah there's a Spanish student that wanted you to do it with me as well so I I got her





### 00:35:37



name but she's not taking so she's kind of like an internship um in fact what I will do is like at the end of the term as I always do we will do a launch all of us so you can yeah what is she studying so she's study I think she's studying computer science actually in was she Barcelona I'm not sure but she came here for three or four months she's working oh the um on the I think so Yeah.





### 00:36:07



And then but but then she has to so the her report is due in January which is much half of your project essentially she's doing she doesn't have much time. Uh yeah I'm also meeting her. I'd love to meet her. Yeah. Yeah. Yeah. Um so now you and her are kind of doing more the healthcare uncertainty stuff and is doing kind of something completely different.





### 00:36:34



In that case, I'd actually even like to meet up quicker because then we can discuss what our problems are with each other. Yeah. I mean, she's looking at something. She's looking at different aspect of things. But it's still CP, isn't it? It's still CP, but in a different setting. Ashwin is not doing on CP.





### 00:36:51



Yeah, she he still on CP. Yeah. Because he told me he's doing on fintech or something from No. So, he he is doing a financial problem. Okay. But it is a CP, but his setting is very different because he cannot use like a split CP or anything like this because he he doesn't have exchangeability because he's looking at time series.





### 00:37:14



Um, but we're going to meet together at some point and then you guys will all talk to each other. That's the that's what I like to do. It's really good because Ashman and I met um when when did we meet? Last week, last Monday. Uhhuh. And I was telling him, "Oh yeah, Mary's how how I know you." And yeah,





### 00:37:34



I didn't tell him that I Yeah. So, how are you? Are you 100% recovered from your Well, still have the cough. Uhhuh. Are we doing we we this Thursday? Yes. Yes. Okay, cool. This is this Thursday is on promo of uh just discussion group and next Thursday is a lecture. So this to so this Thursday is the Suma one, right? Okay. Nice. I was there. Yes, I was sick. Yeah, it was really good. Okay, so I'll be there then.





### Transcription ended after 00:38:15



*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*
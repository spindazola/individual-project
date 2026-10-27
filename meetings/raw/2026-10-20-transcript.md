# Nery Meeting 2 — 20 October 2026 — Raw Transcript

> Preserved from the meeting notes supplied in ChatGPT. Computer-generated transcript; may contain transcription errors.

## 00:00:00

Okay. Does that make sense? Um, no. Can you can you repeat? So like so there's multilabels data from the checkbook data set and how would I just essentially try there are many images that only have one label. Yeah. Look at a vector of one and zero.

## 00:00:25

Right. You say if this patient has cardio it has a one it have if it has low opacity it has one as well and so forth right so there are images for which you have only one one if that makes sense one disase turn yeah soify all of those cases a frequency of the label that we have yeah for those yeah okay yes okay that makes sense only single labels Okay.

## 00:00:57

And then um calibration test should be done at patient level then or image level. I would say I'm leaning towards image level. Right. Patient set should be uh well we need to go right. So this is a very good thing. So this is the sort of thing that we need to try.

## 00:01:19

So I suggest we try both. Okay. Okay. So I think that like what I mentioned before the whole the the whole idea of this project yeah to elucidate how how this different calibration decision affects overall coverage and and efficiency at the end okay so we can have two things to calibrate by patient calibrate by uh images right actually I'm going to go back on what I said and I think I would expect it's easier to do by patient rather than Yeah.

## 00:01:50

Yeah. I think with all of this knowledge that you will gather, you will be able to write like a very nice tutorial on how to use these ideas practically on clinical program not kind of like a general intro. Yeah. But for doctors absolutely so we could methodology methodologically what makes sense it should do it by patient because ultimately we want to make a decision about patient.

## 00:02:17

Um but then we can see right if you do this right how much you do actually going to pay for this methodological decision. Yeah. Right. So so that that's one thing that we can check right. So the other thing that you will see very quickly now when you get your hands dirty with the data is that there are images that are frontal images and there are images that are like lateral images.

## 00:02:43

Yep. Okay. And then the question is um what happens in the calibration we only have frontals and in real life you will have like a mix of frontal and lateral right are you actually accurately representing reality is that good know right so we can have like a one one of the experiments that you will run will have a mix of lateral and frontal calibration set another one could have only cell for example and so on right yeah that make sense yes and then you're having like a one strong pipeline and you will be tweaking around the calibration procedures and then

## 00:03:19

explain what like what how how each decision decision affects the final coverage and the final efficiency of your perform predictor, right? Okay. Because I see that some sometimes like some decision might look good in terms of coverage but then they pay horribly badly in terms of efficiency. So when I say the value means the size of the prediction region that you get in this case will be sets right.

## 00:03:46

the size of the sets also. Yeah. Um and then yeah so essentially it is having a predictor having the conformal pipeline and then having different approaches to calibration and then having one way to actually measure the quality of your predictor and that's usually coverage efficiency and then one thing is like the air condition coverage. Yeah.

## 00:04:11

Right. So remember we discussed this kind of what you get out of prediction is like the general the average coverage guarantee the marginal coverage what we call it. Yeah usually want conditional coverage which is much a much stronger claim but that is impossible theoretically. Yeah. Um but we could approximate. I'm just discussing all of this stuff so that we can initiate what the whole picture is.

## 00:04:37

Okay. Um in terms of next steps just going back to to shortsight things again. So in instead of uh so in terms of next steps will be report and then starting to cook out the data and then computing some general statistics how many do we have like sing for the single cases how many do we have of how many do we have for each of these conditions right there.

## 00:05:02

Yeah. Okay. Um yeah report number two was on checkpoint itself. All of this analysis that you unveiled on the data will go into that one. Okay. Yeah. Um the other thing was have you got time to had have any feedback um on the first report that initial brief thing? Yes, I need to give you that.

## 00:05:31

Um, unless let's discuss that next time. Okay, that's fine. There isn't anything terribly urgent there. Yeah, the only thing we we already um solidified something actually. We already kind of did it, didn't we? We actually went through it last week. Sorry. Yeah. Yeah. Yeah.

## 00:05:50

So, okay, that's fine. Um um and I've been building my literature. So I think I'm going at a like a steady pace. It's just like um I don't really have much to say right now. Just like things are a bit slow and then eventually everything's going to happen at once and it's going to be fun.

## 00:06:17

Um yeah, but for them you need to be healthy yourself, right? just take care of yourself, you know, drink a lot of water and have your meds if you're drinking milk. Hopefully, you're taking your meds, right? And rest. Yeah. Okay. So, I'm going to let you rest now and I'll see you next week.

## 00:06:40

Lecture. Yeah. Okay. Yeah. You need to rest for the lecture then. Yes. Yeah. Um Yeah. What? I think I have it in my calendar. It's very good that we talked about this. It's at 6 30. Okay, perfect. That's perfect.

## 00:07:01

Yeah, that's really good. Um, okay. So, I'll see you this Thursday then. Uh, and I hope you feel better by then. Really? Yes. Um, I was supposed to go for this conference tomorrow, but I might not go. Um, you will do good to rest. Yeah. Cool.

## 00:07:19

So, we'll see. Um, and I'll give you the food on Thursday instead of because I I bought it on Thursday, but then you said you weren't there. Yeah. Sorry about that. I thought it was 6:30 today last time, but seven was a bit late for me. Yeah. I have a wife and a dog.

## 00:07:35

Yes. Okay. Um, well, yeah, sorry. Thank you very much for being so accommodating. I mean, this will happen. This happens when you work together with people, you know. sometimes in time making sometime actually I was writing you an email when you sent me your message telling you that I was late uh so yeah so we we should be able to accommodate these things it's not a problem so no we are having fun and working today and that's um okay so take care of yourself I'll see you on Thursday yeah we'll catch up soon bless you God bless you too bye-bye

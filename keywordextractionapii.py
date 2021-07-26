from monkeylearn import MonkeyLearn

ml = MonkeyLearn('43c8ebbd128987b0ac9fdcd8869d3974ded4ffe9')
data = ["Elon Musk has shared a photo of the spacesuit designed by SpaceX. This is the second image shared of the new design and the first to feature the spacesuit’s full-body look."]
model_id = 'ex_YCya9nrn'
result = ml.extractors.extract(model_id, data)
print(result.body)
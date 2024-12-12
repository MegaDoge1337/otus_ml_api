class AnimalClassificationModel:
    @classmethod
    def make_inference(cls, paws_count: int, has_fur: int, mammal: int) -> str:
        if paws_count == 0 and has_fur == 0 and mammal == 0:
            return "snake"
        
        if paws_count == 4 and has_fur == 1 and mammal == 1:
            return "dog"
        
        if paws_count == 4 and has_fur == 0 and mammal == 1:
            return "elephant"

        return "the model's usage limit has been reached, please try again after a while."

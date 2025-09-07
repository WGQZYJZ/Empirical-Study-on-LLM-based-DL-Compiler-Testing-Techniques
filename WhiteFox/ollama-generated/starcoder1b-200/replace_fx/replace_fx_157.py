
class Model(torch.nn.Module):
    def __init__(self, fallback_random=True):
        super().__init__()
        if torch.cuda.is_available():
            self.linear = torch.nn.Linear(2, 2).cuda()
        else:
            self.linear = torch.nn.Linear(2, 2)

        # Random fill the input tensor with random values in float64
        if fallback_random or torch.cuda.is_available():
            self.input_tensor = torch.rand_like(__output__)
    ...

# Initializing the model
m = Model()
m(x1).data
__output__.data


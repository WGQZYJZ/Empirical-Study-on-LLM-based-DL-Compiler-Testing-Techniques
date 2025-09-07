
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None, **kwargs):
        if x2 is not None:
            tensor1, tensor2 = x1, x2
            assert isinstance(tensor1, Tensor), "Input of Model 'forward' must be a Tensor."
            assert isinstance(tensor2, Tensor), "Input of Model 'forward' must be a Tensor."
            return t1 + t2
        else:
            return self.linear(x1)


# Initializing the model
m = Model()



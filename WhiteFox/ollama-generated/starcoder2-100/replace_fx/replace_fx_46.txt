
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # noqa: B904, F821
        torch.nn.functional.dropout(x1)

        # the following line won't erase it because of fallback_random=True (default setting for CPU models), 
        # but will erase if fallback_random is False
        return torch.rand_like(x1, dtype=torch.float32)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(10, 5).cuda() # using `input_args={'device': 'cuda'}` instead of input_tensor={'shape': (None, None)} will erase the dropout node (for GPU models only)

 __output__= m(x1)


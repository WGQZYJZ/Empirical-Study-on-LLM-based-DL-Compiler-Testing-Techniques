
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, inplace=False) # Apply dropout to the input tensor
        v2 = torch.rand_like(x1, dtype=torch.float64, device='cuda')
        return v2


# Initializing the model
m = Model()
# Setting configuration for fallback_random function (the random function will not be replaced)
gm.config(fallback_random=True)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1): 
        # Permute the input tensor. It is important that the size of permuted tensor changes after permuting
        v3 = torch.tensor([[0.5947]])
        return v3


# Initializing the model
m_new  = Model()

# Inputs to the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permuted tensor A
        v2 = x2.permute(0, 2, 1) # Permuted tensor B

        t3 = torch.bmm(v1, v2) # Matrix multiplication: (batch_size * out_channel) x (out_channel*in_channel).
        
        return self.linear(t3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2) # Batch 1: input with channel dimension first
x2 = torch.randn(1, 5, 4) # Batch 2: input with channel dimension second

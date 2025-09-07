
class Model(torch.nn.Module):
    def __init__(self, d_model=128):
        super().__init__()
        self.linear = torch.nn.Linear(d_model * 3 + 47, d_model)
 
    def forward(self, input1, input2):
        v1 = torch.cat([input1, input2], dim=-1) # Concatenate the inputs along the last dimension
        v2  = self.linear(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(47, 60, dtype=torch.float32) # Input with a size of [batch_size, sequence_length]
x2 = torch.randn(5, 84, dtype=torch.float32) # Input with a size of [batch_size, d_model * 3 + 47]


# Output from the model

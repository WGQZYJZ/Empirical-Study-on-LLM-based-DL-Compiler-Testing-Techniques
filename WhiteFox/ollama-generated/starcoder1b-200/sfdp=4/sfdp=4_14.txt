
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 10)
 
    def forward(self, x):
        attn = self.attn(x)
        output = attn @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


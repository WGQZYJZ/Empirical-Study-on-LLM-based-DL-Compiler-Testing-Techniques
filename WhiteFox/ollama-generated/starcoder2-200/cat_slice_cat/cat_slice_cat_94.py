
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 2)
 
    def forward(self, x): 
        v1  = torch.cat([x[:, :], x[: ,:]], dim=1)
        v2  = v1[0]
        v4_1 = v1[:,9223372036854775807:] # Slice along dimension 1
        v4 = torch.cat([v2, v4_1], dim=1) # Concatenate along dimension 1
        v3 = self.fc(v4)
        return v3

# Initializing the model
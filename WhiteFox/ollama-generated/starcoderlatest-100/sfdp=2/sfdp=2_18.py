
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 32) # The dimensionality of the query and key should be different for this model.
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x1, x2):
        v1 = self.attention(x1).transpose(-2, -1) @ x2
        v2 = self.dropout(v1)
        return v2


# Inputs to the model
x1 = torch.randn(100, 768, 5, 8) # The dimensionality of the query and key should be different for this model.
x2 = torch.randn(100, 768, 5, 32)

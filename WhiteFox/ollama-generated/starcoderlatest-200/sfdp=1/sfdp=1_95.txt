
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(128, 512)
 
    def forward(self, x):
        # The inputs are transformed by a single linear layer and then fed into the attention mechanism
        qk = F.linear(x, self.query_layer, bias=None).transpose(-2, -1)
        

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 2
        self.inv_scale  = -1 / (4 * 5)
        self.dropout  = torch.nn.Dropout(0.7)
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value, inv_scale_factor=0.25, dropout_p=0.8):
        v  = self.softmax(torch.nn.functional.dropout(torch.matmul(query, key.transpose(-2, -1)) \
                .div(inv_scale_factor), p=dropout_p)).matmul(value)

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(8, 3054, 768)
y1 = torch.randn(8, 768, 768)
y2 = torch.randn(8, 3054, 768)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.1)
 
    def forward(self, x1):
        v1 = torch.matmul(query, key.transpose(-2, -1)) / inv_scale_factor
        softmax_v1 = v1.softmax(dim=-1)
        dropout_v1 = self.dropout(softmax_v1)
        output = dropout_v1.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 32, 64, 64)

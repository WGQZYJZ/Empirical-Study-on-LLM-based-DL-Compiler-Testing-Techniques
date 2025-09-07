
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_v1 = v1.div(0.5)
        softmax_v1 = scaled_v1.softmax(dim=-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        output = dropout_v1.matmul(value)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

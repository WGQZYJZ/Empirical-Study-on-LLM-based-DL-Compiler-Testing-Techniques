
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        scaled_v1 = v1.div_(inv_scale_factor)
        softmax_v1 = scaled_v1.softmax(-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        output = dropout_v1.matmul(x2).sum(-1, keepdim=True)
        return output


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
key1 = torch.randn(1, 8, 15, 15)
__output1 = m(input1, key1)



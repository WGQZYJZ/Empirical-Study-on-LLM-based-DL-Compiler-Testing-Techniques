
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))
        scale_factor = (1 / math.sqrt(qk.size(-2))) * \
            (torch.nn.functional.softmax(qk.mul(scale_factor), dim=-1)) 
        dropout = torch.nn.functional.dropout(scale_factor, p=dropout_p)
        output = dropout.matmul(x1)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

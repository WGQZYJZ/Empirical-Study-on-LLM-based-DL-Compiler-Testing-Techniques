
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 128)
        self.key = torch.nn.Linear(256, 128)
        self.value = torch.nn.Linear(256, 128)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1))
        scaled_qk = qk / math.sqrt(qk.shape[-1])
        softmax_qk = torch.nn.functional.softmax(scaled_qk)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output  = dropout_qk @ self.value(x)
        return output


# Initializing the model
m1 = Model()

# Inputs to the model
x1 = torch.randn(4, 256)

# First run of the model
__output___1__ = m1(x1)

# Second run of the model
x1_2  = x1.clone().detach()
__output___2__ = m1(x1_2)


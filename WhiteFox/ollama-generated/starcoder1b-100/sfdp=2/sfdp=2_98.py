
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 384)
        self.key = torch.nn.Linear(512, 384)
        self.value = torch.nn.Linear(512, 512)
 
    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key.transpose(-2, -1))
        scale_factor = inv_scale_factor / (torch.pow(qk + epsilon, beta))
        scaled_qk = qk.div_(scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        output = dropout_qk.matmul(self.value(x1).matmul(softmax_qk))
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 512)

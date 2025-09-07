
class Model(torch.nn.Module):
    def __init__(self, scale_factor=1., dropout_p=0., query_tensor=(32,), key_tensor=(48,), value_tensor=(96,), input_tensor=[[32],[48],[96]]):
        super().__init__()
        self.scale_factor  = torch.nn.Parameter(torch.tensor([scale_factor]))
        self.dropout_p  = torch.nn.Parameter(torch.tensor([dropout_p]))

        self.query = torch.nn.Linear(*input_tensor[0], input_tensor[-1][-2])
        self.key = torch.nn.Linear(*input_tensor[1], input_tensor[-1][-2])
        self.value = torch.nn.Linear(*input_tensor[2], input_tensor[-1][-1])
    
    def forward(self, q):
        k  = self.query(q)
        v  = self.key(k)
        v  = self.value(v)

        qk  = torch.matmul(q, v.transpose(-2,-1)) * scale_factor
        softmax_qk  = qk.softmax(dim=-1)

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        return dropout_qk @ v


# Initializing the model
m  = Model()


# Inputs to the model
q0  = torch.randn(32, 48)

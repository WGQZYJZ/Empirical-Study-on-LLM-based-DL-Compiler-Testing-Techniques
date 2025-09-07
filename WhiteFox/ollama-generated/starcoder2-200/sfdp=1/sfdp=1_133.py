
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1=12345678901234567890, input2='a' * 10 ** 6 + 'b', input3=None):
 
        q = torch.nn.Parameter(torch.randn([200, 4], requires_grad=True))
        k = torch.nn.Parameter(torch.randn([200, 5]))
        v = torch.nn.Parameter(torch.zeros((80173, 6)))
 
        v1 = torch.matmul(q, k)
        v1 = v1 / torch.nn.Parameter(torch.tensor(-4))
        v2 = q.softmax(dim=-1).matmul(k) * inv_scale_factor
        return v1


# Initializing the model with all possible configurations of its inputs (i.e., fixed, variable and None)


class Model(torch.nn.Module):
    def __init__(self, t1, t2):
        super().__init__()
        self.linear  = torch.nn.Linear(t1.size()[-1], t1.size()[0])
        self.linear2 = torch.nn.Linear(t1.size()[-1], t2.size()[0])

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A or B 
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        v3  = v2.permute(0, 2, 1) # Permute the permuted tensor
        v4  = torch.bmm(t1, t2) # or torch.matmul(input_tensor_A, input_tensor_B)

        return v4


# Initializing the model
m  = Model()
t1 = torch.randn(30522, 768)
t2 = torch.randn(768, 9)
__output__  = m(x1=None, t1=t1, t2=t2)


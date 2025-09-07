
class Model(torch.nn.Module):
    def __init__(self, input_shape=(100,), output_shape=[32]):
        super().__init__()
 
    def forward(self, x):
        v1  = torch.split(x, [50], dim=1) # [torch.Tensor([1483.6973]), torch.Tensor([1482.783])]
        return list((x1.mean(dim=[-1]) for x1 in v1))


m = Model()

x = torch.tensor(np.arange(50).reshape(-1, 1), requires_grad=True) # 50 elements tensor [0 ... 49] 
__output__  = m(x) # A list of two tensors


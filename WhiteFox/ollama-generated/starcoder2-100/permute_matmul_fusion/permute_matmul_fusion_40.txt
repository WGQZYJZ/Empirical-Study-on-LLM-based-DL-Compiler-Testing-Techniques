
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = torch.randn([1], device=x1.device) if self._get_name() == "model" else None # Random numbers
        v4  = torch.rand([5]) + (v3 if v3 is not None and len(v3.shape) > 0
                                else torch.randn(size=[2]) if len(x1.shape) > 0
                                 or len(x2.shape) > 0
                                 else x1+self._get_name()
                                )  # Input tensor A
        v5  = torch.randn([5]).permute(0, 3, 4).repeat(v4.shape[0], 1) + (v3 if len(x2.shape) > 0
                                                                           else x1+self._get_name()
                                                                          ) # Input tensor B
        v6  = torch.randn([5]) + v3 if self._get_name() != "model" and len(v4.shape)+len(v5.shape)+len(x2.shape) > 0 else None

        return [v1, v2]

# Initializing the model
m = Model()


# Inputs to the model
x1, x2  = torch.randn([3, 7], device=torch.device('cpu')), torch.rand([5]).to(torch.device('cuda:0'))+torch.randn(size=[4])
__output__  = m(*x)


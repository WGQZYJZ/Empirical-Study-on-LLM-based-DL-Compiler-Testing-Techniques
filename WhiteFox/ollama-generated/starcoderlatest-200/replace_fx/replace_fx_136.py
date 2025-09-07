
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Use the low-memory implementation of dropout (replace_fx=lowmem_dropout)
        v1 = torch.nn.functional.dropout(x1, p=0.5, inplace=True)

        # Use random numbers as a replacement for any dropout operation (inplace=False)
        v2 = torch.rand_like(x1, 
                              dtype=v1.dtype, 
                              layout=v1.layout, 
                              device=v1.device, 
                              requires_grad=v1.requires_grad)

        return v1, v2

# Inputs to the model
x1 = torch.randn(4, 5, 5)

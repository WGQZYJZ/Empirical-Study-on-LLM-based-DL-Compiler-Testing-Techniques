
class Model(torch.nn.Module):
    def __init__(self, num_elements):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2 = torch.cat([v1 for i in range(num_elements)], dim=0) 
        return v2

# Initializing the model with different number of elements. The input tensors have the same shape as that of `x` in the following code:
m  = Model(3).to("cuda") # Use GPU to compute the results


__inputs1__ = torch.randn(20, 48) # Input tensor for multiplication with size (N, 72)
__inputs2__ = torch.randn(256, 96) # Input tensor for concatenation with size (N, 32*3)
__output__  = m(__inputs1__, __inputs2__).to("cuda")


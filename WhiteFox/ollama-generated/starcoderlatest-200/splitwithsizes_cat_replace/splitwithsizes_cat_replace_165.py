
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 3) # Split into three tensors
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=0) # Concatenate these split tensors along the zeroth dimension
 
        return c1


# Optimizing the model with different inputs and checking their validity with `is_valid_splitwithsizes_cat`
for __input__ in (torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64)):
    print(f'Valid: {is_valid_splitwithsizes_cat(__model__, __input__)}\n')

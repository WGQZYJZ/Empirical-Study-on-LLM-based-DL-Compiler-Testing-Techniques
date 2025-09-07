
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 1], 1, dtype=torch.float32) 
        v2 = convert_element_type(v1, torch.float64) 
        v3 = torch.cumsum(v2, 1) 
        return v3


# Test case 1: Static graph with TensorRT engines

User: 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, key, query, value):
        k_expand = torch.unsqueeze(key, -1).repeat((1, 1, key.shape[2], 1))
        v_expand = torch.unsqueeze(value, -1).repeat((1, 1, 1, value.shape[2]))
        scale_factor = torch.matmul(query, k_expand) / math.sqrt(torch.einsum("nc,nc->n", query, k_expand))
        softmax_kernel = scale_factor.softmax(-1)
        kernel = (softmax_kernel * math.sqrt(value.shape[-1])).unsqueeze(-1)
        v2  = self.conv(x1)
        conv_output  = torch.matmul(v2, kernel)
        return conv_output

# Initializing the model
m = Model()



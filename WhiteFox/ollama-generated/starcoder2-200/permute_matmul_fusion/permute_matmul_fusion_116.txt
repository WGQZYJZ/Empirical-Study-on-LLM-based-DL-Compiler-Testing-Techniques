
class Model(torch.nn.Module):
    def __init__(self, x1 = 200000):
        super().__init__()

    def forward(self, x1, y1):

        v1 = torch.tensor(x1.permute(0, -3).flatten(), dtype=torch.float) # Permute the input tensor A

        if torch.cuda.is_available():
            v2  = torch.bmm(v1[..., None], y1[None].to('cuda')).reshape(-1, x1.shape[-4], x1.shape[-3], x1.shape[-2]) # or torch.matmul(v1[..., None], y1)
        else:
            v2  = torch.bmm(v1[..., None], y1[None]).reshape(-1, x1.shape[-4], x1.shape[-3], x1.shape[-2]) # or torch.matmul(v1[..., None], y1)

        v5 = torch.nn.functional.linear(v2[:, 0].permute(0, -1), torch.tensor([[0., 0.], [0., 0.]], dtype=torch.float32)).reshape(-1,) # Apply linear transformation to the permuted tensor
        return v5

# Initializing the model: x1 = torch.randn(10, 4, 3) and y1 = torch.randn(x1.shape[0], 3, 4), which is a tensor of the same shape with the random values.
m_output  = Model()(torch.randn(5, 200000, 600, 80))


class Model(torch.nn.Module):
    def __init__(self,
                 dim_q: int,
                 dim_k: int,
                 dim_v: int,
                 heads: int = 8,
                 dropout_p: float = 0.1) -> None:
        super().__init__()
        self.dim_q = dim_q
        self.dim_k = dim_k
        self.dim_v = dim_v
        self.heads = heads
 
        # Convolution layer for the query tensor, key tensor and value tensor of each attention head
        self.conv1 = torch.nn.Conv2d(3, 8 * heads, kernel_size=1, stride=1, padding=0)

        self.attn = torch.nn.MultiheadAttention(
            embed_dim=self.dim_v, 
            num_heads=self.heads
        )
 
        # Linear layer to map the output of each attention head into a new tensor
        self.fc = torch.nn.Linear(self.dim_v * heads, dim_q)
 
    def forward(self, x1):
        v1 = self.conv1(x1)  # (N, 8, H, W) --> (N, 64, 64)

        _, q, k, v = self.attn(query=v1, key=v1, value=v1)  # Multihead attention
        softmax_qk = q / math.sqrt(self.dim_q)

        output = torch.matmul(softmax_qk, v)  # (N, H, d_k) x (N, d_k, d_v) --> (N, H, d_v)
        output = self.fc(output.reshape(-1, output.shape[-1])).unsqueeze(0)

        return output
 
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
model = Model(dim_q=5, dim_k=8, dim_v=64, heads=2).to("cuda")

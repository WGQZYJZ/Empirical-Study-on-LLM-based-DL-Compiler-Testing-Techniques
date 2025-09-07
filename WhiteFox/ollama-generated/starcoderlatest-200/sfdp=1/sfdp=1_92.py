
class Attention(torch.nn.Module):
    def __init__(self, num_heads=16, dim_per_head=32, scale_factor=16):
        super().__init__()
        self.num_heads = num_heads
        self.dim_per_head = dim_per_head
        self.scale_factor = scale_factor

        # We need to initialize the input tensor with an arbitrary value since torch.conv2d requires its input
        # tensor's shape is set when the kernel size and stride are both 1. But, if we just use nn.Conv2d
        # here, then it only works for small inputs because it uses "SAME" padding method to compute the output
        self.query = torch.nn.Parameter(torch.randn(dim_per_head, 1, kernel_size=1, stride=1))
        self.key = torch.nn.Parameter(torch.randn(dim_per_head, num_heads, kernel_size=1, stride=1))

        # Apply a linear transformation to the input tensor and then split it into heads (split the output of
        # the linear transformation by `num_heads`) so that each head can compute its attention separately
        self.attn_out = torch.nn.Linear(dim_per_head * num_heads, 1)

    def forward(self, x):
        bs, nq, _h, _w = x.shape

        # The input tensor is reshaped so that each batch and height of the image in the first axis has shape [bs, nq, h, w]
        qk = self.query.repeat([bs, nq, 1]) * (x.view(-1, _h, _w).view(bs * nq, -1))

        # Compute a single linear transformation to combine the query and key tensors, then split it into heads
        attn_out = self.attn_out(qk)  # [bs*nq, 1]
        attn_out = attn_out.view(-1, self.num_heads).contiguous().unsqueeze(dim=-2)  # [bs*nq, nq, h, w]

        key = torch.nn.functional.unfold(self.key, kernel_size=kernel_size, stride=stride)
        attn_out = attn_out * (x / (self.scale_factor**2))  # [bs*nq, nq, h, w]

        softmax_qk = torch.nn.functional.softmax(attn_out, dim=-3)  # [bs*nq, nq, h, w]
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # [bs*nq, nq, h, w]

        output = torch.nn.functional.fold(dropout_qk * key, kernel_size=(1, dim_per_head), stride=stride)  # [bs, nq, h, w]
        return output

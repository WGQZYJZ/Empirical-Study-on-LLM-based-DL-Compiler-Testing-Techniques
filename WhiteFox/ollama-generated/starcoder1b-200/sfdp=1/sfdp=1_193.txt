
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 3)
 
    def forward(self, x1):
        batch_size, seq_len, input_size = x1.shape
        batch_size  *= 4
        seq_len     *= 2
        input_size   *= 5
        batch_size, seq_len, input_size = int(batch_size), int(seq_len), int(input_size)
        x1            = torch.arange(0, batch_size).view(batch_size, seq_len).float().cuda() / float(input_size - 1)
        query         = torch.randn(batch_size, seq_len, input_size).normal_()  # Random inputs to the linear layer
        key           = torch.randn(seq_len, input_size, input_size).normal_()  # Random inputs to the linear layer
        output        = self.linear(x1.view(batch_size * seq_len, -1))  # Compute dot product of x and y
        attn          = torch.bmm(output.unsqueeze(-2), key)                   # Get attention coefficients
        value         = torch.randn(seq_len, batch_size, input_size).normal_()  # Random inputs to the linear layer
        attn *= dropout_p  # Apply dropout after dot product is calculated
        return attn

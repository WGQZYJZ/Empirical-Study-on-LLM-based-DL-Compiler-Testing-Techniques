
class Attention(nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1, activation="relu"):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead

        self.conv = nn.Conv2d(3*6*self.d_model//self.nhead, 8, 1, stride=1, padding=0)
        self.norm = nn.LayerNorm(self.d_model)
 
        def build_attn():
            self.build_layer()
            self.attention_weights_drop = nn.Dropout(dropout)

        self.query, self.key, self.value  = map(
            lambda t: Parameter(torch.Tensor(t)), [
                (self.d_model, nhead, d_model // nhead),
                (self.d_model, nhead, d_model // nhead),
                (self.d_model//nhead, nhead)]
        )

        self.attn = nn.MultiheadAttention(self.key, self.value)

    def forward(self):
        x1  = self.conv()
        v2  = x1  * 0.5 # Multiply the output of the convolution by 0.5
        v3  = v1  * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
        v4  = torch.erf(v3) # Apply the error function to the output of the convolution
        v5  = v4 + 1 # Add 1 to the output of the error function
        v6  = v2 * v5 # Multiply the output of the convolution by the output of the error function

        
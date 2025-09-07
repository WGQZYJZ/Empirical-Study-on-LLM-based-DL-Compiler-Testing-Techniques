
class TransformerEncoderLayer(nn.Module):
    def __init__(self,d_model=512, nhead=8, dim_feedforward=2048, dropout=0.1)
        super().__init__()
 
        self.conv  = nn.Conv2d(3, 8, 1, stride=1, padding=1)

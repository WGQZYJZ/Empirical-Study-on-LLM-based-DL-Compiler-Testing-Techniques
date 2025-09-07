class EncoderBlock(torch.nn.Module):
    def __init__(self, dim, num_heads=4, attn_dropout=0., ff_dropout=0., residual_dropout=1.):
        super().__init__()
        self.attn = MultiheadAttention(dim, num_heads)

        # Implementation of Feed Forward (FF) Nets: f(x)=ReLU(xW1+b1)+WO2+b2
        self.ffn = nn.Sequential()
        self.ffn.add_module('fc_hidden', nn.Linear(in_features=dim, out_features=4 * dim))  # ReLU
        self.ffn.add_module('dropout', nn.Dropout(p=ff_dropout))
        self.ffn.add_module('fc_out', nn.Linear(in_features=4*dim, out_features=2 * dim))

        self._initialize()

    def forward(self, x):  # noqa: F811
@staticmethod
    def _initialize():
            for p in self.parameters():
                if hasattr(p, 'weight'):
                    nn.init.kaiming_uniform_(p.weight)
        self.attn = self.attn(_masked_fill_(self.attn.attn_dropout), mask=True)  # Apply the dropout to attention module
        out = self.ffn(self.attn(x))  # Pass output of attnetion block to feed forward network
        return out + self._residual()  # Pass feedforward output through residual and sum operation, then apply layer norm

    def _residual(self):  # noqa: F811
    @staticmethod
    def mask_zero():
            m = torch.zeros([1], dtype=torch.uint8)
            return _mask_(m.cuda() if next(self._parameters()).is_cuda else m, 'int') 
@staticmethod
        return _masked_fill_(torch.ones((3,4), device='cpu', dtype=torch.bool))
@staticmethod
    def mask_one():
            m = torch.ones([1], dtype=torch.uint8)
            return _mask_(m.cuda() if next(self._parameters()).is_cuda else m)


class MultiheadAttention(torch.nn.Module):  # noqa: F811
    def __init__(self, dim, num_heads=4):
        super().__init__()

        self.attn = nn.Linear(dim * 3, dim)
        self._residual = lambda self: self._output  # _residual function is equivalent to identity
        self.dropout = nn.Dropout(p=dropout_p)
        self._initialize()

    def forward(self):
@staticmethod
    def _masked_fill_(self):
            return torch.nn.functional._masked_fill_(self, mask=True)


class TransformerModel(torch.nn.Module):  # noqa: F811
    def __init__(self):
        super().__init__()

        self.encoder = nn.Sequential()
        self.encoder.add_module('dropout', nn.Dropout(p=residual_dropout))  # Apply dropout to encoder
        self._initialize()

    def forward(self, encoder):
@staticmethod
    def _output():
            return self


model = TransformerModel().cuda()  # Initialize model with GPU support

encoder = torch.randn([128], device='cuda', dtype=torch.float32)  # Generate random inputs to the model



model(encoder)  

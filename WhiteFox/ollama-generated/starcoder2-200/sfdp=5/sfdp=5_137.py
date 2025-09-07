
class TransformerModel(torch.nn.Module):
    def __init__(self,
                 input_dim,
                 dim,
                 nhead=8,  # The number of heads in self-attention layer
                 num_encoder_layers=12,  # Number of encoder layers
                 dropout=0.,
                 **kwargs
                ):
        super().__init__()
 
        self.src_mask = None
 
 
    def make_encoder_padding_mask(self):
 
        src_mask  = torch.zeros((nbatches, 1, 1, self._tgt_len)).to(device)
        src_mask[:, -seq_length:] = float('-inf')
        return src_mask
 
 
    
    def forward(self, src: Tensor):
        if self.src_mask is None or self.src_mask.size(0) != len(src):
            device  = src.device
            batch_size  = src.size(1)
            
            src_mask  = self.make_encoder_padding_mask()
            self._cache['self_attn_mask'] = src_mask
 
        # encoder
        enc = self.encoder(self._cache, src, src)
        # decoder
        dec = self.decoder(self._cache, src)
 
    
        return dec
 

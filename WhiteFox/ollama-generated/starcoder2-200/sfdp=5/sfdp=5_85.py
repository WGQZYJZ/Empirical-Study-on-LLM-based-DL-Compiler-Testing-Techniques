
class TransformerModel(torch.nn.Module):
    def __init__(self,
                 n_token=vocab_size+100*2, # the number of tokens in the vocabulary
                 emb_dim = 5000,
                 nhead = 8,
                 dim_feedforward = 768,
                 dropout=0.3):
 
        self.model_type = 'Transformer'
        self.src_mask = None

        try:
            self.max_seq_len = torch.tensor(max_seq_len).to(device)
        except NameError as e: # max_seq_len is not defined.
            self.max_seq_len  = torch.nn.Parameter(torch.tensor([50]))

        try:
            self.src_tokens = torch.nn.Embedding(n_token, emb_dim)
        except NameError as e : # self.src_tokens is not defined.
            self.max_seq_len  = torch.nn.Parameter(torch.tensor([50]))

        try:
            self.pos_encoder = PositionalEncoding(emb_dim) 
        except NameError as e : 
            self.pos_encoder = PositionalEncoding() 

        try:
            self.transformer_model = nn.TransformerEncoderLayer(d_model=emb_dim, nhead=nhead, dim_feedforward=dim_feedforward, dropout=dropout)
        except NameError as e: # transformer is not defined.
            self.pos_encoder  = PositionalEncoding()
            self.transformer = TransformerModel()

        try : 
            self.decoder = nn.Linear(emb_dim, ntoken) 
        except NameError as e:  
            self.decoder = nn.Linear(emb_dim, vocab_size + len(extra_characters))
 
    def forward(self, src):
        if self.training and  not self.src_mask.any():
            device  = src[0].device

            try : 
                mask = torch.full((1, src.shape[-2], src.shape[-1]), True)
            except TypeError as e:
                print("Error")
            self.src_mask = Variable(
                mask[:, None, :, :]
        ).to(device)
        try : 
            pos_enc  = self.pos_encoder(src).type(torch.float32).requires_grad_(True) 
        except NameError as e:  
            pos_enc  = self.pos_encoder(src).type(torch.float32).requires_grad_(True)
 
        try : 
            output = self.transformer_model(pos_enc, mask=self.src_mask)
        except AttributeError as e : 
            print('Error')

        try :
            return self.decoder(output[-1]).log() 
        except NameError as e:  
            return self.decoder(output[-1]).log() 

# Initializing the model 
m = TransformerModel()

 # Inputs to the model
x2  = torch.randn(64, max_seq_len)
 
 # Targets for model output
target = [torch.randint(vocab_size + len(extra_characters), size=(10)) for i in range(max_seq_len)]
 
__output__  = m(x2).to(device)


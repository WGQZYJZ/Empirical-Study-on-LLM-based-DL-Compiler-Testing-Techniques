
class TransformerModel(torch.nn.Module):
    def __init__(self, nhead=128):
        super().__init__()
 
        # Embeddings for each positional sequence index. The embedding layer is followed by a batch normalization layer to normalize the values in the embedding layer.
        self.position_embeds = torch.nn.Embedding(30000 + 5, 768)
        self.pos_layer1 = torch.nn.Linear(768, 24)
 
        # Embeddings for each query sequence index. The embedding layer is followed by a batch normalization layer to normalize the values in the embedding layer.
        self.query_embeds = torch.nn.Embedding(3000 + 5, 768)
        self.pos_layer2 = torch.nn.Linear(768, 19)
 
        # Layer for computing the dot product of the query sequence and the key sequence after concatenating them into a single sequence. This layer is followed by two batch normalization layers to normalize the values in each sequence.
        self.qk_layer = torch.nn.Linear(2 * 768, nhead)
 
        # Layer for computing attention weights based on the dot product of the query and key sequences. This layer is followed by a dropout layer that drops out some of the input units during training to prevent overfitting.
        self.attn_layer = torch.nn.Linear(nhead * 768, 32)
 
        # Layer for computing the dot product of the attention weights and the value sequence. This layer is followed by a batch normalization layer that normalizes the values in each sequence after this computation.
        self.out_layer1 = torch.nn.Linear(32 + nhead * 768, 51)
 
        # Layer for computing the dot product of the attention weights and the value sequence. This layer is followed by a batch normalization layer that normalizes the values in each sequence after this computation.
        self.out_layer2 = torch.nn.Linear(32 + nhead * 768, 51)
 
        # Layer for computing the dot product of the attention weights and the value sequence. This layer is followed by a batch normalization layer that normalizes the values in each sequence after this computation.
        self.out_layer3 = torch.nn.Linear(32 + nhead * 768, 51)
 
        # Layer for computing the dot product of the attention weights and the value sequence. This layer is followed by a batch normalization layer that normalizes the values in each sequence after this computation.
        self.out_layer4 = torch.nn.Linear(32 + nhead * 768, 51)
 
        # Layer for computing the dot product of the attention weights and the value sequence. This layer is followed by a batch normalization layer that normalizes the values in each sequence after this computation.
        self.out_layer5 = torch.nn.Linear(32 + nhead * 768, 51)
 
    def forward(self, x):
 
        # Applying the position embedding to the sequence of indices corresponding to the input tensor. The embedding layer is followed by a batch normalization layer to normalize the values in each sequence.
        pos_embeds = self.position_embeds(x[:, :, 0]) / math.sqrt(768)
        pos1_embeds = self.pos_layer1(pos_embeds)
 
        # Applying the query embedding to the sequence of indices corresponding to the query tensor. The embedding layer is followed by a batch normalization layer to normalize the values in each sequence.
        q_embeds = self.query_embeds(x[:, :, 0]) / math.sqrt(768)
        pos2_embeds = self.pos_layer1(q_embeds)
 
        # Computing dot product of the query and key sequences, followed by a batch normalization layer to normalize the values in each sequence after computing the dot products.
        qk  = torch.nn.functional.normalize(self.qk_layer(torch.cat([pos1_embeds[:, None], pos2_embeds[:, None]], dim=1)), p=2, dim=-1)
 
        # Applying dropout to the output of the dot product layer to prevent overfitting during training
        attn = self.attn_layer(qk).sigmoid()

        # Computing the dot product of the attention weights and the value sequence after multiplying it by a constant scalar factor. The values in each sequence are normalized using batch normalization before computing these operations.
        out1  = torch.nn.functional.normalize((self.out_layer1(torch.cat([pos2_embeds[:, None], pos_embeds[:, None] * attn[:, :, None]], dim=1))).sigmoid(), p=2, dim=-1)

        # Computing the dot product of the attention weights and the value sequence after multiplying it by a constant scalar factor. The values in each sequence are normalized using batch normalization before computing these operations.
        out2  = torch.nn.functional.normalize((self.out_layer2(torch.cat([pos1_embeds[:, None], pos_embeds[:, None] * attn[:, :, None]], dim=1))).sigmoid(), p=2, dim=-1)
 
        # Computing the dot product of the attention weights and the value sequence after multiplying it by a constant scalar factor. The values in each sequence are normalized using batch normalization before computing these operations.
        out3  = torch.nn.functional.normalize((self.out_layer3(torch.cat([pos2_embeds[:, None], pos1_embeds[:, None] * attn[:, :, None]], dim=1))).sigmoid(), p=2, dim=-1)

        # Computing the dot product of the attention weights and the value sequence after multiplying it by a constant scalar factor. The values in each sequence are normalized using batch normalization before computing these operations.
        out4  = torch.nn.functional.normalize((self.out_layer4(torch.cat([pos2_embeds[:, None], pos1_embeds[:, None] * attn[:, :, None]], dim=1))).sigmoid(), p=2, dim=-1)

        # Computing the dot product of the attention weights and the value sequence after multiplying it by a constant scalar factor. The values in each sequence are normalized using batch normalization before computing these operations.
        out5  = torch.nn.functional.normalize((self.out_layer5(torch.cat([pos2_embeds[:, None], pos1_embeds[:, None] * attn[:, :, None]], dim=1))).sigmoid(), p=2, dim=-1)

        return [out1, out2, out3, out4, out5]
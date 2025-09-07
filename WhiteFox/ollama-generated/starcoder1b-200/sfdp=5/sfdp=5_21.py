The input of the model is a set of vectors, one for each row and column of `attn_mask`, where rows are from the sequence and columns are from the embedding matrix (the input for each transformer layer). In this case, `num_layers` corresponds to the number of layers in the transformer, since the `attention_p` argument passed to `Transformer` specifies the dropout probability.


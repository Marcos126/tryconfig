local M = {}

-- Función de mapeo simplificada con descripción
local function map(bufnr, mode, lhs, rhs, desc)
    vim.keymap.set(mode, lhs, rhs, { buffer = bufnr, desc = "LSP " .. desc })
end

M.on_attach = function(client, bufnr)
    -- Mapeos de teclado para funciones LSP
    map(bufnr, 'n', 'gd', vim.lsp.buf.definition, "Go to definition")
    map(bufnr, 'n', 'K', vim.lsp.buf.hover, "Hover symbols")
    map(bufnr, 'n', 'gi', vim.lsp.buf.implementation, "Go to implementation")
    map(bufnr, 'n', '<leader>rn', vim.lsp.buf.rename, "Rename symbol")
    map(bufnr, 'n', '<leader>ca', vim.lsp.buf.code_action, "Code action")
    map(bufnr, 'n', '[d', vim.diagnostic.goto_prev, "Previous diagnostic")
    map(bufnr, 'n', ']d', vim.diagnostic.goto_next, "Next diagnostic")

    -- Activar resaltado automático al estar en un símbolo
    if client.server_capabilities.documentHighlightProvider then
        vim.api.nvim_create_autocmd('CursorHold', {
            buffer = bufnr,
            callback = function() vim.lsp.buf.document_highlight() end
        })
        vim.api.nvim_create_autocmd('CursorMoved', {
            buffer = bufnr,
            callback = function() vim.lsp.buf.clear_references() end
        })
    end
end

local lspconfig = require("lspconfig")

lspconfig.phpactor.setup({
    on_attach = M.on_attach,
    capabilities = capabilities,
    root_dir = function()
        return vim.fn.getcwd()
    end,
    settings = {
    }
})

lspconfig.tsserver.setup({
    on_attach = M.on_attach,
    capabilities = capabilities,
    root_dir = function()
        return vim.fn.expand('%:p:h')  -- Retorna el directorio del archivo actual
    end,
    settings = {}
})


return M


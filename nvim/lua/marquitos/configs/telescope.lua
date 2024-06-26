local builtin = require('telescope.builtin')

return {
    require('telescope');

    vim.keymap.set('n', '<leader>pf', builtin.find_files, {});
    vim.keymap.set('n', '<C-p>', builtin.git_files, {});
    vim.keymap.set('n', '<leader>ps', builtin.live_grep, {});
    vim.keymap.set('n', '<leader>vh', builtin.help_tags, {});

    require('telescope').setup{
        defaults = {
            file_ignore_patterns  = {"target/*","target","test/*","test","undotree/*","undotree"}
        },
    }
}

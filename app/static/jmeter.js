const api_getdirandscript = '/api/getdirandscript';
const api_runjmeter = '/api/runjmter';


$('.script-tree').on('click', 'button.directory', function () {
    var dirname = dataTrim($(this).text());
    console.log(`dirname=${dirname}`);
    $.get(api_getdirandscript, {dirname: dirname}, function (result) {
        var dirList = result.dirlist;
        var scriptList = result.scriptlist;
        console.log(`dirList=${dirList}`);
        console.log(`scriptList=${scriptList}`);
        var parentDirSelector = $(`button.directory:contains('${dirname}')`);
        var subTree = '<ul class="subtree">';
        for (let x in dirList) {
            subTree += getDirTreeCode(dirList[x]);
        }
        for (let x in scriptList) {
            subTree += getScriptTreeCode(scriptList[x]);
        }
        subTree += '</ul>';
        parentDirSelector.after(subTree);
    })
});


/**
 * 去掉空格、回车、换行
 */
function dataTrim(data) {
    data = data.replace(/ +/g, '');//去掉空格
    data = data.replace(/[ ]/g, '');//去掉空格
    data = data.replace(/[\r\n]/g, '');//去掉回车换行
    return data
}


function getDirTreeCode(dirname) {
    return `
<li>
    <label>
        <input class="checkbox-inline" value="${dirname}" type="checkbox"/>
    </label>
    <button class="directory" type="button">
        <i class="iconfont icon-folder"></i>${dirname}
    </button>
</li>
`
}


function getScriptTreeCode(scriptname) {
    return `
<li>
    <label>
        <input class="checkbox-inline" value="${scriptname}" type="checkbox"/>
    </label>
        <i class="iconfont icon-script"></i>${scriptname}
</li>
`;
}
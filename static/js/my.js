var app = new Vue({
	el: '#app',
	data: {
		loading: false,
		stop_loading:false,
		target: '',
		field127:'',
		sendDisabled:true,
		dialogFormVisible: false,
		form: {
          apikey: '',
          apisercret: '',
        },
        formLabelWidth: '120px'
	},
	mounted() {
		// this.setData()
	},
	methods: {
		start_upload() {
			// this.loading = true
			pywebview.api.start_transfer(this.target).then(() => {})

		},
		api_configuration() {
			this.dialogFormVisible = true
		},
		apt_confirm(){
			pywebview.api.apiconfiguration(this.form.apikey,this.form.apisercret).then(() => {})
			this.dialogFormVisible = false
		},
		clear_content(){
			this.field127 = ""
		},
		stop_search(){
			pywebview.api.stop_search().then(() => {})
		},
		register(){
			pywebview.api.register().then(data => {
				if (data=== 200) {
					this.sendDisabled = false;
					this.$notify({
						title: '注册成功',
						message: '现在可以开始转换了',
						type: 'success',
						position: 'bottom-right'
			});
				}
			})
		},
		openFile() {
			pywebview.api.openFile().then((text) => {
				this.target = text
			})
		},
		openSuccess() {
			this.$notify({
				title: '转换完成',
				message: '转换完成，可以自行修改',
				type: 'success',
				position: 'bottom-right'
			});
		},
		starterror(){
			this.$notify.warning({
				title: '错误',
				message: '接口配置错误',
				position: 'top-left'
			});
		},
		openError() {
			this.$notify.warning({
				title: '错误',
				message: '请先上传音频',
				position: 'top-left'
			});
		},
		setData() {
			pywebview.api.return_data().then(data => {
				this.field127 = data
			})
		}
	}
})

window.addEventListener('pywebviewready', function () {
	console.log('pywebview API初始化完成')
})
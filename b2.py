from b2sdk.v2 import InMemoryAccountInfo, B2Api




def get_api():


    aplication_key_id = "4f043b1b4313"
    aplication_key = "0038b95b84aeccbc48391ab5da4a00b5c1c0d74bb5"

    info = InMemoryAccountInfo()
    api = B2Api(info)

    api.authorize_account("production",aplication_key_id,aplication_key)

    return api


def upload_profile_pic(name,data,todatabase):
    api = get_api()

    bucket= api.get_bucket_by_name("image-profile-pic")
    bucket_name = bucket.name

    delete_old_versiond(bucket_name,name)

    file_data=data.read()
    bucket.upload_bytes(file_data,name)

    download_url = api.account_info.get_download_url()
    file_url = f"{download_url}/file/{bucket_name}/{name}"

    todatabase(name,file_url)



def delete_old_versiond(bucket,file_name):
    api = get_api()
    bucket = api.get_bucket_by_name(bucket)


    print(f"Checking for file versions in bucket: {bucket.name}, file: {file_name}")
    file_versions = list(bucket.ls(file_name,latest_only=False))

    if not file_versions:
        print("noooo")
        return

    for file_versions in file_versions[1:]:
        print("deleting")
        bucket.delete_file_version(file_versions.file_id,file_versions.file_name)





def upload_song(name,cover,audio,tobase,title):
    api = get_api()

    bucket_song = api.get_bucket_by_name("audio-song")
    bucket_cover = api.get_bucket_by_name("image-single")

    bucket_song_name = bucket_song.name
    bucket_cover_name = bucket_cover.name

    file_song_name = f"{name}-{title}"
    file_cover_name = f"{name}-{title}"

    delete_old_versiond(bucket_song_name,file_song_name)
    delete_old_versiond(bucket_cover_name,file_cover_name)

    bucket_song.upload_bytes(audio,file_song_name)
    bucket_cover.upload_bytes(cover,file_cover_name)

    download_url = api.account_info.get_download_url()

    song_url = f"{download_url}/file/{bucket_song_name}/{file_song_name}"
    cover_url = f"{download_url}/file/{bucket_cover_name}/{file_cover_name}"

    tobase(name,title,song_url,cover_url)
    